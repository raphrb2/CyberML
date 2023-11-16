import pandas as pd
import sklearn as sk
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

from mlsecu.data_exploration_utils import *
from mlsecu.data_preparation_utils import *


def get_list_of_attack_types(dataframe):
    if dataframe is None:
        return None
    return get_unique_values(dataframe, "attack_type")


def get_nb_of_attack_types(dataframe):
    if dataframe is None:
        return None
    return len(get_list_of_attack_types(dataframe))


def get_list_of_if_outliers(dataframe, outlier_fraction):
    df_cleaned = remove_nan_through_mean_imputation(dataframe)
    df_one_hot_encoded = get_one_hot_encoded_dataframe(df_cleaned)
    iforest = IsolationForest(contamination=outlier_fraction, random_state=42)
    predictions = iforest.fit_predict(df_one_hot_encoded)
    outlier_indices = df_one_hot_encoded[predictions == -1].index.tolist()
    return outlier_indices

def get_list_of_lof_outliers(dataframe, outlier_fraction):
    df_cleaned = remove_nan_through_mean_imputation(dataframe)
    df_one_hot_encoded = get_one_hot_encoded_dataframe(df_cleaned)
    lof = LocalOutlierFactor(contamination=outlier_fraction)
    predictions = lof.fit_predict(df_one_hot_encoded)
    outlier_indices = df_one_hot_encoded[predictions == -1].index.tolist()
    return outlier_indices

def get_nb_of_if_outliers(dataframe, outlier_fraction):
    return len(get_list_of_if_outliers(dataframe, outlier_fraction))

def get_nb_of_lof_outliers(dataframe, outlier_fraction):
    return len(get_list_of_lof_outliers(dataframe, outlier_fraction))

def get_list_of_parameters(dataframe):
    return get_column_names(dataframe).tolist()

def get_nb_of_occurrences(dataframe):
    return get_nb_of_rows(dataframe)

def get_nb_of_parameters(dataframe):
    return get_nb_of_dimensions(dataframe)