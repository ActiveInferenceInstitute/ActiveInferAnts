module SideCar

using Pkg

# Function to ensure all required packages are installed
function install_dependencies()
    # Activate a temporary environment
    Pkg.activate(temp=true)
    
    # Add RxInfer explicitly
    Pkg.add("RxInfer")
    
    # Add the local MountainCarAI package
    Pkg.develop(path="../MountainCarAI")
    
    # Instantiate to install all dependencies
    Pkg.instantiate()
end

# Function to run MountainCarAI and save outputs
function run_and_save()
    # Ensure we're using the correct project environment
    Pkg.activate("../MountainCarAI")
    
    # Instantiate to ensure all dependencies are installed
    Pkg.instantiate()
    
    # Run the MountainCarAI example script
    include("../MountainCarAI/examples/run.jl")
    
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
