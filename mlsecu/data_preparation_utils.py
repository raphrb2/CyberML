import numpy as np
import pandas as pd
import sklearn as sk

def get_one_hot_encoded_dataframe(dataframe):
    if dataframe is None:
        return None
    return pd.get_dummies(dataframe)

def remove_nan_through_mean_imputation(dataframe):
    if dataframe is None:
        return None
    for column in dataframe.select_dtypes(include=[int, float]).columns.tolist():
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
    return dataframe