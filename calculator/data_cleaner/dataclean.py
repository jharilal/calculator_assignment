"""This module is used to clean data for the calculator webapp"""


class DataClean:
    """This cleans up the values from the input form"""

    @staticmethod
    def data_process(raw_data):
        value_tuple = DataClean.data_screener(raw_data)
        if len(value_tuple) == 0:
            return ValueError
        return value_tuple

    @staticmethod
    def data_screener(uncleaned_values):
        uncleaned_values = str(uncleaned_values)
        split_values = DataClean.data_splitter(uncleaned_values)
        stripped_values = DataClean.data_stripper(split_values)
        float_list = DataClean.float_filter(stripped_values)
        values_tuple = DataClean.list_to_tuple(float_list)
        return values_tuple

    @staticmethod
    def data_splitter(un_split):
        return un_split.split(',')

    @staticmethod
    def data_stripper(list_of_split):
        cleaned_list = []
        for item in list_of_split:
            temp_item = item.strip(" ")
            if temp_item.isnumeric():
                cleaned_list.append(temp_item)
        return cleaned_list

    @staticmethod
    def float_filter(cleaned_data):
        float_data = []
        for item in cleaned_data:
            float_data.append(float(item))
        return float_data

    @staticmethod
    def list_to_tuple(cleaned_float_list):
        return tuple(cleaned_float_list)
