import configparser
import os, shutil


def get_config_from_file(mode: str = "") -> configparser.ConfigParser | list:
    """Gets the config data from the file.

    Args:
        mode (str): is the mode in which the data is returned, "title" returning only sections.
    """
    config = configparser.ConfigParser()
    if not os.path.isfile(f"{os.getcwd()}/setup/config.ini"):
        shutil.copy(
            f"{os.getcwd()}/setup/config_example.ini", f"{os.getcwd()}/setup/config.ini"
        )
    config.read(f"{os.getcwd()}/setup/config.ini")

    return config.sections() if mode == "sections" else config
