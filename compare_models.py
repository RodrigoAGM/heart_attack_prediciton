from pandas import read_csv, DataFrame
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np
from itertools import permutations
import csv

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


def normalize_data(x):
    normalization = MinMaxScaler().fit_transform(X=x)
    return DataFrame(data=normalization, columns=x.columns)


def standardize_data(x):
    standarization = StandardScaler().fit_transform(X=x)
    return DataFrame(data=standarization, columns=x.columns)


# First we read the dataframe to use
data = read_csv('data.csv', na_values=['?', ''])
data = handle_missing(data)

# Get column names
x_cols = list(data.columns)[:10]
y_cols = list(data.columns)[10]

# Get data
X = data[x_cols]
Y = data[y_cols]

# Apply feature scaling
X = standardize_data(X)

# Get train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

nums = list(np.arange(1, 10, 1))
rates = list(np.arange(0.3, 0.8, 0.1))
iterations = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]

# Open csv file with headers
f = open("Results.csv", "w")
fnames = ['Layers', 'Result', 'Rate', 'Iterations']
writer = csv.DictWriter(f, lineterminator='\n',fieldnames=fnames)
writer.writeheader()

k = 10
kfold = KFold(n_splits=k)
# Model with only one hidden layer

layers = [tuple(i) for i in permutations(nums, 1)]
for layer in layers:
    for i in iterations:
        for rate in rates:
            model = MLPClassifier(hidden_layer_sizes=layer, max_iter=i, learning_rate_init=rate, activation='logistic')
            scores = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1_macro')
            mean = np.mean(scores)
            writer.writerow({'Layers' : str(layer), 'Result': str(mean), 'Rate': str(rate), 'Iterations' : str(i)})
            del model
            del scores
            del mean

# Model with two hidden layers
layers = [tuple(i) for i in permutations(nums, 2)]

for layer in layers:
    for i in iterations:
        for rate in rates:
            model = MLPClassifier(hidden_layer_sizes=layer, max_iter=i, learning_rate_init=rate, activation='logistic')
            scores = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1_macro')
            mean = np.mean(scores)

            writer.writerow({'Layers' : str(layer), 'Result': str(mean), 'Rate': str(rate), 'Iterations' : str(i)})
            del model
            del scores
            del mean

# Model with three hidden layers
layers = [tuple(i) for i in permutations(nums, 3)]

for layer in layers:
    for i in iterations:
        for rate in rates:
            model = MLPClassifier(hidden_layer_sizes=layer, max_iter=i, learning_rate_init=rate, activation='logistic')
            scores = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1_macro')
            mean = np.mean(scores)

            writer.writerow({'Layers' : str(layer), 'Result': str(mean), 'Rate': str(rate), 'Iterations' : str(i)})
            del model
            del scores
            del mean

print("FINISHED....")
