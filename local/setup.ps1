# Create a Python virtual environment named 'boringchess'
python -m venv boringchess

# Activate the virtual environment
# For Windows
.\boringchess\Scripts\Activate.ps1

# For Unix or MacOS
# source boringchess/bin/activate

# Install Python modules from requirements.txt
pip install -r local/requirements.txt

# Install WSL2

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --install
