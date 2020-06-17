from pandas import read_csv, DataFrame
from sklearn.neural_network import MLPClassifier
import numpy as np


def handle_missing(dataframe):

    # Print details of the dataframe columns
    print(dataframe.describe())

    # Now we check for all the missing data in the dataframe
    print("\nMissing values")
    print(dataframe.isna().sum())

    # The columns slope, ca and thal have most of its data missing
    # Remove slope, ca and thal from the dataframe

    del_col = ["slope", "ca", "thal"]
    dataframe.drop(del_col, inplace=True, axis=1)

    # Replace the Nan cells with the column's mean

    dataframe.fillna(dataframe.mean(), inplace=True)

    # Check the new dataframe
    print("\nNew Dataframe")
    print(dataframe.head(10))
    print("\nMissing values")
    print(dataframe.isna().sum())

    return dataframe