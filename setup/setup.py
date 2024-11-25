import pathlib
from .config import get_config_from_file

def setup() -> dict:
    create_folders()

def create_folders():
    pathlib.Path(f"{pathlib.Path.cwd()}/audios").mkdir(exist_ok=True)
    pathlib.Path(f"{pathlib.Path.cwd()}/screenshots").mkdir()