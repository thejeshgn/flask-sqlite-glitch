#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".virtualenv" ];
then
    echo ".virtualenv folder exists. Installing using pip"
else
    echo "creating .virtualenv and install using pip"
    python3.7 -m venv .virtualenv
fi

# Activate virtual env
. .virtualenv/bin/activate

# Upgrade the PIP
pip install --upgrade pip
pip install -r requirements.txt
# Work done. so deactivate the virtual env
deactivate
