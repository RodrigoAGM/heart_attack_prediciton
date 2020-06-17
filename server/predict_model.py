from sklearn.neural_network import MLPClassifier
from pandas import read_csv, DataFrame
from sklearn.preprocessing import StandardScaler
from server.utils import handle_missing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np

class Model:

    def __init__(self):
        data = read_csv('server/data.csv', na_values=['?', ''])
        data = handle_missing(data)

        # Get column names
        x_cols = list(data.columns)[:10]
        y_cols = list(data.columns)[10]

        # Get data
        X = data[x_cols]
        Y = data[y_cols]

        self.scaler = StandardScaler()
        # Apply feature scaling
        standarization = self.scaler.fit_transform(X=X)
        X = DataFrame(data=standarization, columns=X.columns)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        self.model = MLPClassifier(hidden_layer_sizes=(4,2), max_iter=10, learning_rate_init=0.4, activation='logistic')
        
        k = 10
        kfold = KFold(n_splits=k)
        scores = cross_val_score(self.model, X_train, Y_train, cv=kfold, scoring='accuracy')
        self.mean = np.mean(scores)

        self.model.fit(X_train, Y_train)
    
    def predict(self, features):

        data = DataFrame(data = features, index=[0])
        data = self.scaler.transform(data)

        return self.model.predict(data)
