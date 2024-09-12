# Check and install required packages
using Pkg

required_packages = ["LibGit2", "HTTP", "JSON"]

for package in required_packages
    if !haskey(Pkg.project().dependencies, package)
        println("Installing $package...")
        Pkg.add(package)
    end
end

# Now import the required packages
using LibGit2
using HTTP
using JSON

# Function to clone the repository
function clone_repo(url, local_path)
    try
        LibGit2.clone(url, local_path)
        println("Repository cloned successfully to $local_path")
    catch e
        println("Error cloning repository: $e")
    end
end

# Function to fetch repository information
function get_repo_info(repo_url)
    api_url = replace(repo_url, "github.com" => "api.github.com/repos")
    try
        response = HTTP.get(api_url)
        return JSON.parse(String(response.body))
    catch e
        println("Error fetching repository information: $e")
        return nothing
    end
end

# Main script
function main()
    repo_url = "https://github.com/sustia-llc/MountainCarAI"
    local_path = "MountainCarAI"

    # Clone the repository
    clone_repo(repo_url, local_path)

    # Get repository information
    repo_info = get_repo_info(repo_url)

    if repo_info !== nothing
        # Describe the repository
        println("\nRepository Description:")
        println("Name: $(get(repo_info, "name", "N/A"))")
        println("Description: $(get(repo_info, "description", "N/A"))")
        println("Stars: $(get(repo_info, "stargazers_count", "N/A"))")
        println("Forks: $(get(repo_info, "forks_count", "N/A"))")
        println("Language: $(get(repo_info, "language", "N/A"))")
        println("Last updated: $(get(repo_info, "updated_at", "N/A"))")

        # Print README content
        readme_path = joinpath(local_path, "README.md")
        if isfile(readme_path)
            println("\nREADME Content:")
            println(read(readme_path, String))
        else
            println("\nREADME.md not found in the repository.")
        end
    end
end

# Run the main function
main()
