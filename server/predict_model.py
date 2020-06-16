from sklearn.neural_network import MLPClassifier
from pandas import read_csv, DataFrame
from server.utils import standardize_data, handle_missing

class Model:

    def __init__(self):
        self.data = read_csv('server/data.csv', na_values=['?', ''])
        self.data = handle_missing(self.data)

        # Get column names
        self.x_cols = list(self.data.columns)[:10]
        self.y_cols = list(self.data.columns)[10]

        # Get data
        self.X = self.data[self.x_cols]
        self.Y = self.data[self.y_cols]

        # Apply feature scaling
        self.X = standardize_data(self.X)

        self.model = MLPClassifier(hidden_layer_sizes=(4,2), max_iter=10, learning_rate_init=0.4, activation='logistic')
        self.model.fit(self.X, self.Y)
    
    def predict(self, features):

        data = DataFrame(data = features)
        return self.model.predict(data)
