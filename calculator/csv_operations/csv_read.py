"""Reads csv files """

import pandas as pd
from calculator.csv_operations.path_finder import  abs_path_to_csv


class CsvRead:
    """Class is built to read csv files"""
    @staticmethod
    def csv_to_df(csv_to_convert):
        """Converts a csv file into a dataframe"""
        pathway = abs_path_to_csv(csv_to_convert)
        return pd.read_csv(pathway)


