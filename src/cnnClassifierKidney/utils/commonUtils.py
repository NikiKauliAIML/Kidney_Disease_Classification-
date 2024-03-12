# Here implements some common function that used in our entire code


# ConfigBox
# It used to direct use of data variable like
# d1 = ConfigBox({'k1':'v1'})
# d1.k1 -> o/p = v1


import os
from box.exceptions import BoxValueError
import yaml
import joblib
import json
from cnnClassifierKidney import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Create a function that used for read YAML file
# So here used ensure_annotation- bcz it take excate parameter type to run the function

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Reads yaml file and returns

    Args: 
        Path_to_yaml(str): path input

    Raises:
        ValueError: is yaml file is empty
        e: empty file

    Returns:
        ConfigBox: Config type
    """ 

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbosr = True):
    """Create a list of directories

    Args:
        path_to_directories (list): List of path of all directories
        ignore_log(bool, optional): ingonre if multiple  dire is to be present
    
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbosr:
            logger.info(f"Directory is created at path: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data

    Args:   
        path(Path): give path to json file
        data(dict): data to be save in json as form of dict
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Json file saved at path: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


# It needed when user upload file for prediction that time need to decode and encode image

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())