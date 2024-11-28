import os
import pathlib
import choice

from .config import get_config_from_file


def setup() -> dict:
    runnning = True
    data = get_config_from_file()
    selected_section = "subreddit"

    while runnning:
        sections = get_config_from_file("sections")

        item, act = choice.Menu(
            choices=sections,
            actions=["edit", "reset"],
            global_actions=["save", "discard"],
            title="Choose an entry and what to do with it or continue.",
        ).ask()
        match act:
            case "edit":
                selected_section = item
                keys = []
                for _key, _value in data.items(item):
                    keys.append(_key)

                key_choice = choice.Menu(
                    choices=keys,
                    actions=["edit"],
                    global_actions=["back"],
                    title=f"Choose a key to edit in the '{item}' section.",
                ).ask()
                if isinstance(key_choice, tuple) and key_choice[1] == "back":
                    continue
                new_value = choice.Input(
                    f"New value? Current for [{item}][{key_choice}]: {data[item][key_choice]}  **Leave blank to keep current"
                ).ask()
                data[item][key_choice] = new_value

            case "save":
                if choice.Binary("Are you sure you want to save?").ask():
                    with open(
                        f"{os.getcwd()}/setup/config.ini", "w", encoding="utf-8"
                    ) as configfile:
                        if data:
                            data.write(configfile)
                    runnning = False

            case "exit":
                if choice.Binary("Are you sure you want to discard?").ask():
                    data = get_config_from_file()
                    runnning = False

    create_folders()

    return {section: dict(data.items(section)) for section in data.sections()}


def create_folders():
    pathlib.Path(f"{pathlib.Path.cwd()}/audios").mkdir(exist_ok=True)
    pathlib.Path(f"{pathlib.Path.cwd()}/screenshots").mkdir(exist_ok=True)
