import logging
import os
from box.exceptions import BoxValueError
import yaml
from chickenClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


def create_directories(path_to_directories: list, verbose=True):
    """

    :param path_to_directories: list of path of directories
    :param verbose:
    :return:
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at :: {path}")
    except Exception as ex:
        logger.error(f"failed to create directories:: {ex}")


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """

    :param path_to_yaml: path like input
    :return:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty!")
    except Exception as ex:
        logger.error(f"failed to read yaml :: {ex}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """

    :param path: path to json file
    :param data: data to be save in json file
    :return:
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f)
        logger.info("successfully data save info json file!")
    except Exception as ex:
        logger.error(f"failed to save json data :: {ex}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """

    :param path: path of json file
    :return:
    """
    try:
        with open(path) as file:
            content = json.load(file)
        logger.info("successfully load json data!")
        return ConfigBox(content)
    except Exception as ex:
        logger.error(f"failed to load json file :: {ex}")


def decodeImage(imgstring, filename):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(filename, 'wb') as f:
            f.write(imgdata)
            f.close()
    except Exception as ex:
        logger.error(f"failed to decodeImage :: {ex}")


def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as ex:
        logger.error(f"failed to encodeImageIntoBase64 :: {ex}")

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
