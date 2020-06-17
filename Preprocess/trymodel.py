from pandas import read_csv, DataFrame
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
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
scaler = StandardScaler()

standarization = scaler.fit_transform(X=X)
X = DataFrame(data=standarization, columns=X.columns)

# Get train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = MLPClassifier(hidden_layer_sizes=(4,2), max_iter=10, learning_rate_init=0.4, activation='logistic')

k = 10
kfold = KFold(n_splits=k)
scores = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='f1_macro')
mean = np.mean(scores)

model.fit(X_train, Y_train)

print("Precision: ", mean)

print(list(Y_test))
print(model.predict(X_test))


data = { 'age':     [32], 
        'sex':      [1], 
        'cp':       [4], 
        'trestbps': [118],
        'chol':     [529],         
        'fbs':      [0],
        'restecg':  [0],
        'thalach':  [130],
        'exang':    [0],
        'oldpeak':  [0]}


print(DataFrame(data=data))
dataf = DataFrame(data=data)
dataf = scaler.transform(dataf)
print(dataf)
print(model.predict(dataf))
#print(X_train)