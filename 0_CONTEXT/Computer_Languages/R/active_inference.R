#!/usr/bin/env Rscript

# Active Inference Implementation in R
# ====================================
#
# This script implements the Active Inference framework using R's statistical
# computing capabilities and matrix operations.
#
# Usage:
#   Rscript active_inference.R single-agent
#   Rscript active_inference.R ant-colony
#   Rscript active_inference.R demo

# Load required libraries
library(stats)
library(MASS)
library(Matrix)

#' Active Inference Agent Class
#'
#' @field n_states Number of hidden states
#' @field n_observations Number of observation types
#' @field n_actions Number of possible actions
#' @field A_matrix Likelihood matrix p(o|s)
#' @field B_matrix Transition matrices p(s'|s,a)
#' @field C_vector Preferences p(o)
#' @field D_vector Prior beliefs p(s)
#' @field current_beliefs Current belief state
#' @field learning_rate Learning rate for belief updates
#' @field uncertainty_weight Weight for epistemic value
#' @field precision Precision parameter
#' @field output_dir Output directory for results
ActiveInferenceAgent <- R6::R6Class("ActiveInferenceAgent",

  public = list(

    # Constructor
    initialize = function(n_states = 3, n_observations = 3, n_actions = 3,
                         learning_rate = 0.1, uncertainty_weight = 0.1,
                         precision = 1.0, output_dir = "output/single_agent") {

      self$n_states <- n_states
      self$n_observations <- n_observations
      self$n_actions <- n_actions
      self$learning_rate <- learning_rate
      self$uncertainty_weight <- uncertainty_weight
      self$precision <- precision
      self$output_dir <- output_dir

      # Initialize generative model
      self$A_matrix <- private$initialize_likelihood_matrix()
      self$B_matrix <- private$initialize_transition_matrices()
      self$C_vector <- private$initialize_preference_vector()
      self$D_vector <- private$initialize_prior_vector()

      # Initialize beliefs
      self$current_beliefs <- self$D_vector

      # Initialize history
      private$belief_history <- list(self$current_beliefs)
      private$action_history <- c()
      private$observation_history <- c()
      private$free_energy_history <- c()
      private$timestamp_history <- c(Sys.time())

      cat(sprintf("Active Inference Agent initialized with %d states, %d observations, %d actions\n",
                  n_states, n_observations, n_actions))
    },

    # Update beliefs given observation
    update_beliefs = function(observation) {
      if (observation < 1 || observation > self$n_observations) {
        stop(sprintf("Invalid observation index: %d", observation))
      }

      tryCatch({
        # Get likelihood for this observation
        likelihood <- self$A_matrix[observation, ]

        # Bayesian update: posterior = prior * likelihood
        posterior <- self$current_beliefs * likelihood

        # Normalize
        posterior <- posterior / sum(posterior)
        posterior[is.na(posterior)] <- 0  # Handle division by zero

        self$current_beliefs <- posterior

        # Record in history
        private$belief_history <- c(private$belief_history, list(self$current_beliefs))
        private$timestamp_history <- c(private$timestamp_history, Sys.time())

        return(self$current_beliefs)

      }, error = function(e) {
        stop(sprintf("Failed to update beliefs: %s", e$message))
      })
    },

    # Calculate variational free energy
    calculate_vfe = function() {
      # F = E_q[ln q(s) - ln p(o|s)] = -E_q[ln p(o|s)] + E_q[ln q(s)]
      expected_likelihood <- private$calculate_expected_likelihood()
      entropy <- private$calculate_entropy(self$current_beliefs)

      return(-expected_likelihood - entropy)
    },

    # Calculate expected free energy for an action
    calculate_efe = function(action) {
      if (action < 1 || action > self$n_actions) {
        stop(sprintf("Invalid action index: %d", action))
      }

      tryCatch({
        # Predict next beliefs
        predicted_beliefs <- private$predict_beliefs(action)

        # Calculate pragmatic value (surprise about preferred observations)
        pragmatic_value <- private$calculate_pragmatic_value(predicted_beliefs)

        # Calculate epistemic value (information gain)
        epistemic_value <- private$calculate_epistemic_value(predicted_beliefs)

        # Total EFE
        efe <- pragmatic_value - self$uncertainty_weight * epistemic_value

        return(list(
          expected = efe,
          pragmatic = pragmatic_value,
          epistemic = epistemic_value
        ))

      }, error = function(e) {
        stop(sprintf("Failed to calculate expected free energy: %s", e$message))
      })
    },

    # Select action by minimizing expected free energy
    select_action = function() {
      tryCatch({
        efes <- sapply(1:self$n_actions, function(action) {
          efe_result <- self$calculate_efe(action)
          return(efe_result$expected)
        })

        # Select action with minimum expected free energy
        best_action <- which.min(efes)[1]

        return(best_action)

      }, error = function(e) {
        stop(sprintf("Failed to select action: %s", e$message))
      })
    },

    # Execute one step of the perception-action loop
    step = function(observation) {
      # Update beliefs based on observation
      self$update_beliefs(observation)

      # Calculate free energy
      fe <- self$calculate_vfe()
      private$free_energy_history <- c(private$free_energy_history, fe)

      # Select and return action
      action <- self$select_action()
      private$action_history <- c(private$action_history, action)
      private$observation_history <- c(private$observation_history, observation)

      return(action)
    },

    # Get agent statistics
    get_statistics = function() {
      if (length(private$action_history) == 0) {
        return(list(
          total_steps = 0,
          average_free_energy = 0,
          action_distribution = c(),
          final_beliefs = self$current_beliefs,
          total_execution_time = 0
        ))
      }

      total_steps <- length(private$action_history)
      avg_fe <- mean(private$free_energy_history)

      # Action distribution
      action_counts <- table(factor(private$action_history, levels = 1:self$n_actions))
      action_dist <- as.numeric(action_counts / sum(action_counts))

      # Calculate execution time
      if (length(private$timestamp_history) > 1) {
        time_diffs <- diff(as.numeric(private$timestamp_history))
        total_time <- sum(time_diffs)
      } else {
        total_time <- 0
      }

      return(list(
        total_steps = total_steps,
        average_free_energy = avg_fe,
        action_distribution = action_dist,
        final_beliefs = self$current_beliefs,
        total_execution_time = total_time
      ))
    },

    # Save results to output directory
    save_results = function() {
      dir.create(self$output_dir, recursive = TRUE, showWarnings = FALSE)

      # Save configuration
      config <- list(
        n_states = self$n_states,
        n_observations = self$n_observations,
        n_actions = self$n_actions,
        learning_rate = self$learning_rate,
        uncertainty_weight = self$uncertainty_weight,
        precision = self$precision
      )
      write.table(as.data.frame(config), file.path(self$output_dir, "config.txt"),
                 sep = "\t", row.names = FALSE, quote = FALSE)

      # Save statistics
      stats <- self$get_statistics()
      write.table(as.data.frame(stats), file.path(self$output_dir, "statistics.txt"),
                 sep = "\t", row.names = FALSE, quote = FALSE)

      # Save belief history
      if (length(private$belief_history) > 0) {
        belief_matrix <- do.call(rbind, private$belief_history)
        belief_df <- as.data.frame(belief_matrix)
        names(belief_df) <- paste0("State", 0:(ncol(belief_df)-1))
        belief_df$Step <- 0:(nrow(belief_df)-1)
        write.csv(belief_df, file.path(self$output_dir, "belief_history.csv"),
                 row.names = FALSE)
      }

      # Save action history
      if (length(private$action_history) > 0) {
        action_df <- data.frame(
          Step = 0:(length(private$action_history)-1),
          Action = private$action_history,
          Observation = private$observation_history
        )
        write.csv(action_df, file.path(self$output_dir, "action_history.csv"),
                 row.names = FALSE)
      }

      # Save free energy history
      if (length(private$free_energy_history) > 0) {
        fe_df <- data.frame(
          Step = 0:(length(private$free_energy_history)-1),
          FreeEnergy = private$free_energy_history
        )
        write.csv(fe_df, file.path(self$output_dir, "free_energy_history.csv"),
                 row.names = FALSE)
      }

      cat(sprintf("Results saved to %s\n", self$output_dir))
    },

    # Print agent state
    print_state = function() {
      cat("=== Agent State ===\n")
      cat(sprintf("Current Beliefs: [%s]\n",
                 paste(round(self$current_beliefs, 3), collapse = ", ")))
      cat(sprintf("Total Steps: %d\n", length(private$action_history)))
      cat(sprintf("Current Free Energy: %.3f\n", self$calculate_vfe()))
      cat(sprintf("Action History: [%s]\n",
                 paste(head(private$action_history, 10), collapse = ", ")))
      if (length(private$action_history) > 10) {
        cat("...\n")
      }
      cat("===================\n")
    }
  ),

  private = list(

    # Initialize likelihood matrix A (p(o|s))
    initialize_likelihood_matrix = function() {
      matrix <- matrix(0, self$n_observations, self$n_states)

      for (obs in 1:self$n_observations) {
        for (state in 1:self$n_states) {
          # Diagonal structure with noise
          is_diagonal <- (obs == state) ||
                         (obs == ((state - 1) %% self$n_observations) + 1)
          base_prob <- if (is_diagonal) 0.7 else 0.1
          noise <- runif(1, -0.1, 0.1)
          matrix[obs, state] <- max(0, min(1, base_prob + noise))
        }
        # Normalize row
        matrix[obs, ] <- matrix[obs, ] / sum(matrix[obs, ])
      }

      return(matrix)
    },

    # Initialize transition matrices B (p(s'|s,a))
    initialize_transition_matrices = function() {
      matrices <- list()

      for (action in 1:self$n_actions) {
        matrix <- matrix(0, self$n_states, self$n_states)

        for (from_state in 1:self$n_states) {
          row <- rep(0.1, self$n_states)

          # Action-specific transition patterns
          if (action == 1) {
            # Stay action
            row[from_state] <- 0.6
          } else if (action == 2) {
            # Move right
            if (from_state < self$n_states) {
              row[from_state + 1] <- 0.6
            } else {
              row[from_state] <- 0.6  # Stay if at boundary
            }
          } else {
            # Random exploration
            row <- rep(1.0 / self$n_states, self$n_states)
          }

          # Normalize row
          row <- row / sum(row)
          matrix[from_state, ] <- row
        }

        matrices[[action]] <- matrix
      }

      return(matrices)
    },

    # Initialize preference vector C (p(o))
    initialize_preference_vector = function() {
      preferences <- rep(0.1, self$n_observations)

      # Prefer certain observations (e.g., food, safety)
      preferences[1:floor(self$n_observations/2)] <- 1.0

      return(preferences)
    },

    # Initialize prior vector D (p(s))
    initialize_prior_vector = function() {
      return(rep(1.0 / self$n_states, self$n_states))
    },

    # Predict beliefs after taking an action
    predict_beliefs = function(action) {
      b_matrix <- self$B_matrix[[action]]
      predicted <- self$current_beliefs %*% b_matrix
      return(as.vector(predicted))
    },

    # Calculate pragmatic value
    calculate_pragmatic_value = function(predicted_beliefs) {
      pragmatic_value <- 0

      for (state in 1:self$n_states) {
        if (predicted_beliefs[state] > 0) {
          for (obs in 1:self$n_observations) {
            obs_prob <- self$A_matrix[obs, state]
            preference <- self$C_vector[obs]
            pragmatic_value <- pragmatic_value +
                             predicted_beliefs[state] * obs_prob * preference
          }
        }
      }

      return(pragmatic_value)
    },

    # Calculate epistemic value
    calculate_epistemic_value = function(predicted_beliefs) {
      return(private$calculate_entropy(predicted_beliefs))
    },

    # Calculate Shannon entropy
    calculate_entropy = function(beliefs) {
      beliefs <- beliefs[beliefs > 0]  # Remove zero probabilities
      return(-sum(beliefs * log(beliefs)))
    },

    # Calculate expected likelihood
    calculate_expected_likelihood = function() {
      expected_likelihood <- 0

      for (obs in 1:self$n_observations) {
        likelihood <- self$A_matrix[obs, ]
        expected_obs_prob <- sum(self$current_beliefs * likelihood)
        if (expected_obs_prob > 0) {
          expected_likelihood <- expected_likelihood + expected_obs_prob * log(expected_obs_prob)
        }
      }

      return(expected_likelihood)
    },

    # Private fields
    belief_history = NULL,
    action_history = NULL,
    observation_history = NULL,
    free_energy_history = NULL,
    timestamp_history = NULL
  )
)

#' Ant Colony Environment
#'
#' @field grid_size Size of the environment grid
#' @field n_ants Number of ants
#' @field food_sources Number of food sources
#' @field pheromone_decay Pheromone decay rate
#' @field max_steps Maximum simulation steps
#' @field output_dir Output directory
AntColonyEnvironment <- R6::R6Class("AntColonyEnvironment",

  public = list(

    initialize = function(grid_size = 8, n_ants = 5, food_sources = 3,
                         pheromone_decay = 0.95, max_steps = 100,
                         output_dir = "output/ant_colony") {

      self$grid_size <- grid_size
      self$n_ants <- n_ants
      self$food_sources <- food_sources
      self$pheromone_decay <- pheromone_decay
      self$max_steps <- max_steps
      self$output_dir <- output_dir

      # Initialize environment
      self$pheromone_grid <- private$initialize_grid()
      self$food_grid <- private$initialize_grid()
      self$ants <- list()
      self$food_locations <- list()

      # Create food sources
      self$food_locations <- private$create_food_sources()

      # Place food in grid
      for (loc in self$food_locations) {
        self$food_grid[[loc$y]][[loc$x]] <- 10.0
      }

      # Create ants
      for (i in 1:n_ants) {
        pos <- private$get_random_position()
        agent <- ActiveInferenceAgent$new(
          n_states = 4, n_observations = 3, n_actions = 4,
          uncertainty_weight = 0.2, output_dir = file.path(output_dir, "ants")
        )
        ant <- list(
          id = i,
          position = pos,
          agent = agent,
          carrying_food = FALSE,
          energy = 100.0
        )
        self$ants <- c(self$ants, list(ant))
      }

      cat(sprintf("Ant Colony Environment initialized with %d ants on %dx%d grid\n",
                 n_ants, grid_size, grid_size))
    },

    # Run simulation
    run_simulation = function() {
      start_time <- Sys.time()

      for (step in 1:self$max_steps) {
        # Update environment
        self$update_environment()

        if (step %% 10 == 0) {
          total_pheromones <- private$get_total_pheromones()
          food_collected <- sum(sapply(self$ants, function(ant) ant$carrying_food))
          cat(sprintf("Step %d: Pheromones=%.2f, Food=%d\n",
                     step, total_pheromones, food_collected))
        }
      }

      end_time <- Sys.time()
      execution_time <- as.numeric(difftime(end_time, start_time, units = "secs"))

      return(list(
        steps = self$max_steps,
        execution_time = execution_time,
        convergence = private$check_convergence()
      ))
    },

    # Update environment for one step
    update_environment = function() {
      # Decay pheromones
      for (y in 1:self$grid_size) {
        for (x in 1:self$grid_size) {
          self$pheromone_grid[[y]][[x]]$home <- self$pheromone_grid[[y]][[x]]$home * self$pheromone_decay
          self$pheromone_grid[[y]][[x]]$food <- self$pheromone_grid[[y]][[x]]$food * self$pheromone_decay
        }
      }

      # Update ants
      for (i in 1:length(self$ants)) {
        ant <- self$ants[[i]]

        # Generate observation
        observation <- private$generate_observation(ant$position)

        # Step agent
        action <- ant$agent$step(observation)

        # Execute action
        new_position <- private$execute_action(ant$position, action)

        # Lay pheromone
        self$lay_pheromone(ant, new_position)

        # Check for food
        if (self$food_grid[[new_position$y]][[new_position$x]] > 0) {
          ant$carrying_food <- TRUE
          self$food_grid[[new_position$y]][[new_position$x]] <- self$food_grid[[new_position$y]][[new_position$x]] - 1
          ant$energy <- min(100.0, ant$energy + 20.0)
        }

        # Decrease energy
        ant$energy <- max(0.0, ant$energy - 1.0)

        # Update ant in list
        ant$position <- new_position
        self$ants[[i]] <- ant
      }
    },

    # Save results
    save_results = function() {
      dir.create(self$output_dir, recursive = TRUE, showWarnings = FALSE)

      # Save pheromone grid
      pheromone_data <- matrix(0, self$grid_size * self$grid_size, 4)
      colnames(pheromone_data) <- c("Y", "X", "HomePheromone", "FoodPheromone")

      idx <- 1
      for (y in 1:self$grid_size) {
        for (x in 1:self$grid_size) {
          pheromone_data[idx, ] <- c(y-1, x-1,
                                    self$pheromone_grid[[y]][[x]]$home,
                                    self$pheromone_grid[[y]][[x]]$food)
          idx <- idx + 1
        }
      }

      write.csv(pheromone_data, file.path(self$output_dir, "pheromone_grid.csv"),
               row.names = FALSE)

      # Save food grid
      food_data <- matrix(0, nrow = sum(sapply(self$food_grid, function(row) sum(row > 0))), 3)
      if (nrow(food_data) > 0) {
        colnames(food_data) <- c("Y", "X", "FoodAmount")
        idx <- 1
        for (y in 1:self$grid_size) {
          for (x in 1:self$grid_size) {
            if (self$food_grid[[y]][[x]] > 0) {
              food_data[idx, ] <- c(y-1, x-1, self$food_grid[[y]][[x]])
              idx <- idx + 1
            }
          }
        }
        write.csv(food_data, file.path(self$output_dir, "food_grid.csv"),
                 row.names = FALSE)
      }

      # Save individual ant results
      for (ant in self$ants) {
        ant$agent$save_results()
      }

      cat(sprintf("Environment results saved to %s\n", self$output_dir))
    },

    # Get statistics
    get_statistics = function() {
      food_collected <- sum(sapply(self$ants, function(ant) ant$carrying_food))
      total_pheromones <- private$get_total_pheromones()
      average_energy <- mean(sapply(self$ants, function(ant) ant$energy))

      return(list(
        total_ants = length(self$ants),
        food_sources = length(self$food_locations),
        total_pheromones = total_pheromones,
        food_collected = food_collected,
        average_energy = average_energy
      ))
    }
  ),

  private = list(

    # Initialize grid
    initialize_grid = function() {
      grid <- list()
      for (y in 1:self$grid_size) {
        row <- list()
        for (x in 1:self$grid_size) {
          row <- c(row, list(0.0))
        }
        grid <- c(grid, list(row))
      }
      return(grid)
    },

    # Create food sources
    create_food_sources = function() {
      locations <- list()
      for (i in 1:self$food_sources) {
        pos <- private$get_random_position()
        locations <- c(locations, list(pos))
      }
      return(locations)
    },

    # Get random position
    get_random_position = function() {
      return(list(
        x = sample(1:self$grid_size, 1),
        y = sample(1:self$grid_size, 1)
      ))
    },

    # Generate observation for ant
    generate_observation = function(position) {
      x <- position$x
      y <- position$y

      # Check neighboring cells for food and pheromones
      food_nearby <- FALSE
      home_pheromone <- 0.0
      food_pheromone <- 0.0

      for (dy in -1:1) {
        for (dx in -1:1) {
          nx <- x + dx
          ny <- y + dy

          if (nx >= 1 && nx <= self$grid_size && ny >= 1 && ny <= self$grid_size) {
            if (self$food_grid[[ny]][[nx]] > 0) {
              food_nearby <- TRUE
            }
            home_pheromone <- max(home_pheromone, self$pheromone_grid[[ny]][[nx]]$home)
            food_pheromone <- max(food_pheromone, self$pheromone_grid[[ny]][[nx]]$food)
          }
        }
      }

      if (food_nearby) return(1)
      if (food_pheromone > 0.5) return(2)
      if (home_pheromone > 0.5) return(3)
      return(1)  # Default observation
    },

    # Execute action
    execute_action = function(position, action) {
      x <- position$x
      y <- position$y

      new_x <- x
      new_y <- y

      if (action == 1) {  # North
        new_y <- max(1, y - 1)
      } else if (action == 2) {  # East
        new_x <- min(self$grid_size, x + 1)
      } else if (action == 3) {  # South
        new_y <- min(self$grid_size, y + 1)
      } else if (action == 4) {  # West
        new_x <- max(1, x - 1)
      }

      return(list(x = new_x, y = new_y))
    },

    # Lay pheromone
    lay_pheromone = function(ant, position) {
      x <- position$x
      y <- position$y

      if (ant$carrying_food) {
        self$pheromone_grid[[y]][[x]]$food <- min(1.0, self$pheromone_grid[[y]][[x]]$food + 0.1)
      } else {
        self$pheromone_grid[[y]][[x]]$home <- min(1.0, self$pheromone_grid[[y]][[x]]$home + 0.1)
      }
    },

    # Get total pheromones
    get_total_pheromones = function() {
      total <- 0.0
      for (y in 1:self$grid_size) {
        for (x in 1:self$grid_size) {
          total <- total + self$pheromone_grid[[y]][[x]]$home + self$pheromone_grid[[y]][[x]]$food
        }
      }
      return(total)
    },

    # Check convergence
    check_convergence = function() {
      # Simple convergence check - can be made more sophisticated
      return(TRUE)  # Placeholder
    }
  )
)

#' Run single agent demo
run_single_agent_demo <- function() {
  cat("🧠 R Single Agent Active Inference Demo\n")
  cat("=====================================\n")

  # Create agent
  agent <- ActiveInferenceAgent$new(
    n_states = 3,
    n_observations = 3,
    n_actions = 3,
    uncertainty_weight = 0.1,
    output_dir = "output/single_agent"
  )

  cat("Initial beliefs:", paste(round(agent$current_beliefs, 3), collapse = ", "), "\n")
  cat("Generative model shapes:\n")
  cat("  A matrix:", dim(agent$A_matrix), "\n")
  cat("  B matrices:", length(agent$B_matrix), "matrices\n")
  cat("  C vector:", length(agent$C_vector), "\n")
  cat("  D vector:", length(agent$D_vector), "\n\n")

  # Run simulation steps
  observations <- c(1, 0, 2, 1, 0, 2, 1, 0, 2, 1)

  for (i in 1:length(observations)) {
    obs <- observations[i]

    cat("Step", i, "- Observation:", obs, "\n")

    action <- agent$step(obs)
    cat("  Action:", action, "\n")

    beliefs <- agent$current_beliefs
    cat("  Beliefs: [", paste(round(beliefs, 3), collapse = ", "), "]\n")

    fe <- agent$calculate_vfe()
    cat("  Free Energy:", round(fe, 3), "\n\n")
  }

  # Show statistics
  stats <- agent$get_statistics()
  cat("Final Statistics:\n")
  cat("  Total Steps:", stats$total_steps, "\n")
  cat("  Average Free Energy:", round(stats$average_free_energy, 4), "\n")
  cat("  Action Distribution:", paste(round(stats$action_distribution, 3), collapse = ", "), "\n")
  cat("  Final Beliefs:", paste(round(stats$final_beliefs, 3), collapse = ", "), "\n")

  # Save results
  agent$save_results()
  cat("\nResults saved to", agent$output_dir, "\n")
}

#' Run ant colony demo
run_ant_colony_demo <- function() {
  cat("🐜 R Ant Colony Active Inference Demo\n")
  cat("===================================\n")

  # Create environment
  env <- AntColonyEnvironment$new(
    grid_size = 8,
    n_ants = 5,
    food_sources = 3,
    pheromone_decay = 0.95,
    max_steps = 50,
    output_dir = "output/ant_colony"
  )

  cat("Created environment with", env$n_ants, "ants on", env$grid_size, "x", env$grid_size, "grid\n\n")

  # Run simulation
  results <- env$run_simulation()

  # Show final statistics
  stats <- env$get_statistics()
  cat("\nFinal Statistics:\n")
  cat("  Total Pheromones:", round(stats$total_pheromones, 2), "\n")
  cat("  Food Collected:", stats$food_collected, "\n")
  cat("  Average Energy:", round(stats$average_energy, 2), "\n")

  # Save results
  env$save_results()
  cat("\nResults saved to", env$output_dir, "\n")
}

#' Main function
main <- function() {
  args <- commandArgs(trailingOnly = TRUE)

  if (length(args) == 0) {
    cat("Usage: Rscript active_inference.R [single-agent|ant-colony|demo]\n")
    cat("Running both demos...\n\n")
    run_single_agent_demo()
    cat("\n")
    run_ant_colony_demo()
  } else if (args[1] == "single-agent") {
    run_single_agent_demo()
  } else if (args[1] == "ant-colony") {
    run_ant_colony_demo()
  } else if (args[1] == "demo") {
    run_single_agent_demo()
    cat("\n")
    run_ant_colony_demo()
  } else {
    cat("Invalid argument. Use 'single-agent', 'ant-colony', or 'demo'\n")
  }
}

# Run main if script is executed directly
if (!interactive()) {
  main()
}
