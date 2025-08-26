! Active Inference Implementation in Fortran

program active_inference
    implicit none
    
    integer, parameter :: num_states = 4
    integer, parameter :: num_observations = 3
    integer, parameter :: num_actions = 2
    
    real(8), dimension(num_states) :: beliefs
    real(8), dimension(num_observations, num_states) :: a_matrix
    real(8), dimension(num_states, num_actions, num_states) :: b_matrix
    real(8), dimension(num_observations) :: c_vector
    real(8), dimension(num_states) :: d_vector
    
    integer :: cycle, observation, action
    
    ! Initialize
    call initialize_model(beliefs, a_matrix, b_matrix, c_vector, d_vector)
    
    print *, "Fortran Active Inference Demo"
    print *, "Initial beliefs:", beliefs
    
    ! Run simulation
    do cycle = 1, 5
        observation = mod(cycle-1, 3) + 1
        call update_beliefs(beliefs, a_matrix, observation)
        action = select_action(beliefs, b_matrix)
        print *, "Cycle", cycle, ": Observation=", observation, ", Action=", action
        print *, "Beliefs:", beliefs
    end do

contains

    subroutine initialize_model(b, a, b_mat, c, d)
        real(8), dimension(:), intent(out) :: b, c, d
        real(8), dimension(:,:), intent(out) :: a
        real(8), dimension(:,:,:), intent(out) :: b_mat
        
        ! Initialize beliefs (uniform)
        b = 1.0d0 / real(num_states, 8)
        
        ! Initialize A matrix (observation likelihood)
        a = reshape([0.8d0, 0.1d0, 0.1d0, &
                    0.1d0, 0.8d0, 0.1d0, &
                    0.1d0, 0.1d0, 0.8d0], [num_observations, num_states])
        
        ! Initialize B matrix (transition likelihood) - simplified
        b_mat = 0.0d0
        b_mat(:,1,:) = reshape([0.9d0, 0.1d0, 0.0d0, 0.0d0, &
                               0.1d0, 0.9d0, 0.0d0, 0.0d0], [num_states, num_states])
        
        ! Initialize C and D vectors
        c = [0.0d0, 0.5d0, 0.0d0]
        d = [0.5d0, 0.5d0]
    end subroutine

    subroutine update_beliefs(b, a, observation)
        real(8), dimension(:), intent(inout) :: b
        real(8), dimension(:,:), intent(in) :: a
        integer, intent(in) :: observation
        
        real(8), dimension(num_states) :: posterior
        real(8) :: total
        
        ! Bayesian update: P(s|o) ∝ P(o|s) * P(s)
        posterior = a(observation, :) * b
        total = sum(posterior)
        
        if (total > 0.0d0) then
            b = posterior / total
        end if
    end subroutine

    function select_action(b, b_mat) result(action)
        real(8), dimension(:), intent(in) :: b
        real(8), dimension(:,:,:), intent(in) :: b_mat
        integer :: action
        
        ! Simplified action selection
        action = 1  ! Default action
    end function

end program active_inference
