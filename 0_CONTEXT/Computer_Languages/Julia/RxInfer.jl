# Check Julia version
versioninfo()

# Import Pkg module for package management
import Pkg

# Add RxInfer package with specified version
Pkg.add(Pkg.PackageSpec(name="RxInfer", version="3.5.1"))

# Use RxInfer package
using RxInfer

# Display the status of installed packages
Pkg.status()