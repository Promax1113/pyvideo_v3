import configparser
import os


def get_config_from_file(mode: str = "") -> configparser.ConfigParser | list:
    """Gets the config data from the file.

    Args:
        mode (str): is the mode in which the data is returned, "title" returning only sections.        
    """
    config = configparser.ConfigParser()
    config.read(f"{os.getcwd()}/setup/config.ini")

    return config.sections() if mode == "sections" else config
