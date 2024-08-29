import os
import subprocess
import sys

def create_virtualenv(env_name):
    """Create a virtual environment."""
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])

def install_packages(env_name):
    """Install pymdp package."""
    subprocess.check_call([os.path.join(env_name, 'bin', 'pip'), 'install', 'inferactively-pymdp'])

def main():
    env_name = 'venv'
    create_virtualenv(env_name)
    install_packages(env_name)
    print(f"Virtual environment '{env_name}' created and pymdp installed.")

if __name__ == "__main__":
    main()

# source venv/bin/activate
