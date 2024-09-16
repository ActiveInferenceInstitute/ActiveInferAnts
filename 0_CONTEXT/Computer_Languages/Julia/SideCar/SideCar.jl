module SideCar

using Pkg

# Function to ensure all required packages are installed
function install_dependencies()
    # Activate the current directory as the project
    Pkg.activate(".")
    
    # Add RxInfer explicitly
    Pkg.add("RxInfer")
    
    # Instantiate to install all dependencies
    Pkg.instantiate()
end

# Function to run MountainCarAI and save outputs
function run_and_save()
    # Ensure we're using the correct project environment
    Pkg.activate(".")
    
    # Instantiate to ensure all dependencies are installed
    Pkg.instantiate()
    
    # Run the MountainCarAI example script
    include("run.jl")
    
    # Save outputs
    mkpath("output")
    # Implement saving logic here, e.g.:
    # save("output/results.jld2", "results", results)
end

# Main function to execute the SideCar functionality
function main()
    install_dependencies()
    run_and_save()
end

# Execute main function when the script is run
if abspath(PROGRAM_FILE) == @__FILE__
    main()
end

end # module