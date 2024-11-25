from os import getcwd


def get_key_and_name() -> tuple:
    with open(f"{getcwd()}/security/key.env", "r") as f:
        key = f.readline()
        f.close()

    with open(f"{getcwd()}/security/name.env", "r") as f:
        name = f.readline()
        f.close()

    return name, key
