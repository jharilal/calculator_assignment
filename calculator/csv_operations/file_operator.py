"""This holds the class that is responsible for moving the csv files to new directories"""
import shutil


class FileOperator:
    """Contains methods to move files around"""
    @staticmethod
    def move_to_destination(current_csv_file, destination='calculator/tests/csvs_for_operations/output_csv'):
        shutil.move(current_csv_file, destination)

    @staticmethod
    def reset_csv_test(destination='calculator/tests/csvs_for_operations/input_csv'):
        shutil.move('calculator/tests/csvs_for_operations/output_csv/.', destination)
