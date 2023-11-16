import pandas as pd

def get_column_names(dataframe):
    if dataframe is None:
        return None
    return dataframe.columns

def get_nb_of_dimensions(dataframe):
    if dataframe is None:
        return None
    # return the number of columns
    return dataframe.shape[1]
    
def get_nb_of_rows(dataframe):
    if dataframe is None:
        return None
    return dataframe.shape[0]

def get_number_column_names(dataframe):
    if dataframe is None:
        return None
    return list(dataframe.select_dtypes(include=['int64', 'float64']).columns)

def get_object_column_names(dataframe):
    if dataframe is None:
        return None
    return list(dataframe.select_dtypes(include=['object']).columns)

def get_unique_values(dataframe, column_name):
    if dataframe is None :
        return None
    return dataframe[column_name].unique()
