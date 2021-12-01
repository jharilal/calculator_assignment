"""Holds a function to returns the absolute path of a csv file"""

from pathlib import Path


def abs_path_to_csv(filepath):
    """Converts a relative path into an absolute path"""
    return (Path(filepath)).absolute()
