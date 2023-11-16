import pandas as pd

def get_column_names(dataframe):
    if dataframe.empty:
        return []
    return dataframe.columns

def get_nb_of_dimensions(dataframe):
    if dataframe.empty:
        return 0
    return dataframe.shape[0]


def get_nb_of_rows(dataframe):
    if dataframe.empty:
        return 0
    return dataframe.shape[0]

def get_number_column_names(dataframe):
    if dataframe.empty:
        return []
    return len(dataframe.columns)

def get_object_column_names(dataframe):
    if dataframe.empty:
        return []
    return dataframe.select_dtypes(include=['object']).columns

def get_unique_values(dataframe, column_name):
    if dataframe.empty:
        return []
    return dataframe[column_name].unique()
