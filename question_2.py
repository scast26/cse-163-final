import requests
import base64
import json
import pandas as pd
import numpy as np
import plotly.express as px


DATA = 'https://raw.githubusercontent.com/scast26/cse-163'\
       + '-final/main/19332_Spotify_Songs.csv'
CLIENT_ID = 'e762a2d085544fe59a4708a96560a675'
CLIENT_SECRET = 'f1cea31fddc74f63ad4783648a871752'
AUTH_URL = 'https://accounts.spotify.com/api/token'


def filter_data(data):
    """
    This function takes a DataFrame containing songs and their audio
    features, and returns a DataFrame which filters the original
    DataFrame down into songs with a popularity column of 80 or higher.
    """
    data = pd.read_csv(data, encoding='unicode_escape', low_memory=False)
    data['popularity'] = pd.to_numeric(data.popularity, errors='coerce')
    df = data[data['popularity'] >= 80]
    df = df[['popularity', 'name', 'danceability', 'energy', 'key', 'loudness',
            'mode', 'speechiness', 'acousticness', 'instrumentalness',
             'liveness', 'valence', 'tempo']]
    return df


def show_box_plots(data):
    """
    This function takes a DataFrame containing songs and their audio
    features as a parameter. It returns a plot that shows the box and whisker
    plots of all of the features whose values range from zero to one.
    """
    df = data
    df = df.melt(id_vars=["popularity", "name"], var_name="feature")
    filtered = df[(df['feature'] != 'tempo') & (df['feature'] != 'key')
                  & (df['feature'] != 'loudness') & (df['feature'] != 'mode')]
    box_plot = px.box(filtered, x='feature', y='value', color='feature')
    return box_plot


def get_access_token(client_id, client_secret):
    """
    This function takes a user's Spotify Client ID and
    Client Secret, and returns an oAuth token the user
    can use to access Spotify's API.
    """
    # encode client credentials
    message = f'{client_id}:{client_secret}'
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    auth_header = {}
    auth_data = {}
    auth_header['Authorization'] = 'Basic ' + base64_message
    auth_data['grant_type'] = 'client_credentials'

    res = requests.post(AUTH_URL, headers=auth_header, data=auth_data)
    response_object = res.json()
    token = response_object['access_token']
    return token


def compute_quartile(df, column):
    """
    This function takes in a DataFrame of songs and
    audio features, as well as a column (audio feature)
    of interest. It returns a tuple of the first and third
    quartile values for that audio feature.
    """
    q1 = np.percentile(df[column], 25)
    q3 = np.percentile(df[column], 75)
    return q1, q3


def get_recommendations(token, genre, feature, feature_min, feature_max):
    """
    This function takes an oAuth token, a genre of music, an audio feature,
    and an upper and lower bound for the audio feature as parameters. It
    uses the genre provided, and upper and lower feature boundaries to
    make GET request to Spotify's 'Get Recommendations' endpoint. A successful
    API request will create two files: one file is a .json file which contains
    the JSON information about the 20 songs that were recommended. The
    other is a .txt file that contains a simplified list of recommendations
    (the name of the song, artist, and the song's popularity score).
    """
    # Send recommendations request
    endpoint = 'https://api.spotify.com/v1/recommendations?'
    query = f'{endpoint}limit=20&seed_genres={genre}&min_{feature}'\
            + f'={feature_min}&max_{feature}={feature_max}'
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    res = requests.get(query, headers=header)
    recs = res.json()

    # Write JSON results into a new file
    with open(f'{feature}_recs.json', 'w') as j:
        json.dump(recs, j, indent=2)

    # Create a simplified file of recommendations
    score = 0
    with open(f'{feature}_recs.txt', 'w') as t:
        for i in recs['tracks']:
            t.write(f"\"{i['name']}\" by {i['artists'][0]['name']}")
            t.write(f" - {i['popularity']}\n")
            score += i['popularity']
        t.write(f'Average popularity score is: {score/20}')


def main():
    df = filter_data(DATA)

    box_plot = show_box_plots(df)
    box_plot.show()

    token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    min_instr, max_instr = compute_quartile(df, 'instrumentalness')
    min_speech, max_speech = compute_quartile(df, 'speechiness')
    min_live, max_live = compute_quartile(df, 'liveness')
    min_dance, max_dance = compute_quartile(df, 'danceability')

    get_recommendations(token, 'pop', 'instrumentalness', min_instr, max_instr)
    get_recommendations(token, 'pop', 'speechiness', min_speech, max_speech)
    get_recommendations(token, 'pop', 'liveness', min_live, max_live)
    get_recommendations(token, 'pop', 'danceability', min_dance, max_dance)


if __name__ == "__main__":
    main()
