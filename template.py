# This file is require basic template of project

import os
from pathlib import Path 
import logging

# In modular coding always used log module to display the message that why used logging string
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

# Write the project name
project_name = 'cnnClassifierKidney'

# create a some list of file and folder using python programing
# List the all file with folder
list_of_files = [ 
    ".github/workflows/.gitkeep", #here we add aall enviroment variable when cerate CI/CD pipline and push the code to server
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requrirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

# Create a file and folder using path

for filepath in list_of_files:
    filepath = Path(filepath)
    filedr, filename = os.path.split(filepath)

    if filedr !="":
        os.makedirs(filedr, exist_ok=True)
        logging.info(f"Create a directory; {filedr} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 ):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")