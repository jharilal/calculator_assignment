from pathlib import Path


def abs_path_to_csv(filepath):
    return (Path(filepath)).absolute()
