# Do not edit this file
# Install script for installing model on server
# If you want to install the model on your own server, you can use this script
# First check if the following files are in the same directory as this script:
# - model.py
# - config.txt
# - requirements.txt
# - __train__.py
# - __test__.py

if [ -f "model.py" ] && [ -f "config.txt" ] && [ -f "requirements.txt" ] && [ -f "__train__.py" ] && [ -f "__test__.py" ]; then 
    echo "All files found"
else
    echo "Not all files found"
    exit 1
fi

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found"
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "Pip3 could not be found"
    exit 1
fi

# Check if venv exists in current directory
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
else
    echo "Creating virtual environment"
    python3 -m venv venv
fi

# Recieve boolean parameter requirements_changed from running script
if [ "$1" = true ]; then
    echo "Installing requirements"
    # Activate virtual environment
    source venv/bin/activate
    pip3 install -r requirements.txt
fi