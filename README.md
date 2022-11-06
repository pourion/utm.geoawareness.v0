# Digital Twin for Geo-awareness Service
This repository is for the user interface that visualizes a rectangular user-defined airspace, the UAV detection, and the notification system. 

# Installation 

We recommend creating a virtual environment with Python 3.8+ on your local machine for testing this repository. Please follow the instruction below to create the virtual environment for MacOS or Linux. 

1. First install the python package for creating and managing virtual environments 
```
sudo pip install virtualenv virtualenvwrapper
``` 
2. Add the following to the shell startup script:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
(note if you installed `virtualenv` within another `conda` environment the bash file will be at `/home/<you username>/miniconda3/bin/virtualenvwrapper.sh`)


3. Run `source ~/.bashrc` 
4. Create a virtual environment (replace <VIRTUAL_ENVIRONMENT_NAME> with your name of interest)
```
mkvirtualenv <VIRTUAL_ENVIRONMENT_NAME> -p python3.8
``` 
5. To activate the virtual environment, open a terminal and run
```
workon <VIRTUAL_ENVIRONMENT_NAME>
``` 


## Install dependencies 

To nstall dependencies, run the following command from root directory of this repository from the virtual environment your created above. 
```
workon <VIRTUAL_ENVIRONMENT_NAME>
pip install -r requirements.txt
``` 
