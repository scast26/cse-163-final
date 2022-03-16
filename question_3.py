from sklearn.neural_network import MLPClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd


def load_data():
    songs = pd.read_csv('song_dataset.csv', encoding='unicode_escape',
                        low_memory=False)
    songs = songs.dropna()
    songs['popularity'] = pd.to_numeric(songs.popularity, errors='coerce')
    labels = songs['popularity']
    features = songs[['danceability', 'energy', 'key', 'loudness', 'mode',
                      'speechiness', 'acousticness', 'instrumentalness',
                      'liveness', 'valence', 'tempo']]
    return features, labels


def fit():
    features, labels = load_data()
    inputs_train, inputs_test, labels_train, labels_test = \
        model_selection.train_test_split(features, labels, test_size=0.2)
    nnet = MLPClassifier(hidden_layer_sizes=(6, 5), max_iter=1000)
    nnet.fit(inputs_train, labels_train)

    # Predict what the classes are based on the testing data
    predictions = nnet.predict(inputs_test)

    # Print the score on the testing data
    mlp = accuracy_score(labels_test, predictions)*100
    print("MLP Testing Set Score:", mlp)
    error = mean_squared_error(labels_test, predictions)
    print("MSE = ", error)


def kerasfit():
    features, labels = load_data()
    inputs_train, inputs_test, labels_train, labels_test = \
        model_selection.train_test_split(features, labels,
                                         test_size=0.2, random_state=1)

    model = Sequential()
    model.add(Dense(30, input_dim=11))
    model.add(Dense(25))
    model.add(Dense(20))
    model.add(Dense(15))
    model.add(Dense(10))
    model.add(Dense(8))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam',
                  metrics=['accuracy'])
    model.fit(inputs_train, labels_train, epochs=20, batch_size=10)

    predictions = model.predict(inputs_test)
    error = mean_squared_error(labels_test, predictions)
    print("MSE = ", error)


def skfit():
    features, labels = load_data()
    inputs_train, inputs_test, labels_train, labels_test = \
        model_selection.train_test_split(features, labels,
                                         test_size=0.2, random_state=1)

    model = DecisionTreeRegressor()
    model.fit(inputs_train, labels_train)

    DecisionTreeRegressor()
    predictions = model.predict(inputs_test)
    error = mean_squared_error(predictions, labels_test)
    print("MSE =", error)


def main():
    print('skfit function:')
    skfit()
    print("---------------------------------------------------")
    print('fit function:')
    fit()
    print("---------------------------------------------------")
    print('keras fit function:')
    kerasfit()


if __name__ == "__main__":
    main()
