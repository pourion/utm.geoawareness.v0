# Digital Twin for Geo-Awareness Service
This repository is a basic geo-awareness service with a simple graphical user interface that visualizes a rectangular user-defined airspace, UAV detection, and a notification system.

# Installation 

We recommend creating a virtual environment with Python 3.8+ on your local machine for testing this repository. Please follow the instruction below to create the virtual environment for MacOS or Linux. 

1. First install the python package for creating and managing virtual environments 
```
sudo pip install virtualenv virtualenvwrapper
``` 
2. Add the following to the shell startup script, either `.bashrc` (Linux) or `.bash_profile` (MacOS):
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
To find the path to `virtualenvwrapper.sh` you can use: 
```
find / -name virtualenvwrapper.sh
```
 You should also use the corresponding `python3` installation accompanying the virtual environment.

3. Run `source ~/.bashrc` or `source ~/.bash_profile` 
4. Create a virtual environment (replace <VIRTUAL_ENVIRONMENT_NAME> with a proper name)
```
mkvirtualenv <VIRTUAL_ENVIRONMENT_NAME> -p python3.8
``` 
5. To activate the virtual environment, open a terminal and run
```
workon <VIRTUAL_ENVIRONMENT_NAME>
``` 


## Install dependencies 

To install dependencies, first activate the virtual environment you just created for this project and then run the following command from root directory of this repository:
```
workon <VIRTUAL_ENVIRONMENT_NAME>
pip install -r requirements.txt
``` 
