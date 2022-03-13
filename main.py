import requests
import base64
import json
import pandas as pd
import numpy as np


DATA = 'https://raw.githubusercontent.com/scast26/cse-163'\
       + '-final/main/19332_Spotify_Songs.csv'
CLIENT_ID = 'e762a2d085544fe59a4708a96560a675'
CLIENT_SECRET = 'f1cea31fddc74f63ad4783648a871752'
AUTH_URL = 'https://accounts.spotify.com/api/token'


def filter_data(data):
    data = pd.read_csv(data, encoding='unicode_escape', low_memory=False)
    data['popularity'] = pd.to_numeric(data.popularity, errors='coerce')
    df = data[data['popularity'] >= 90]
    df = df[['popularity', 'name', 'danceability', 'energy', 'key', 'loudness',
            'mode', 'speechiness', 'acousticness', 'instrumentalness',
             'liveness', 'valence', 'tempo']]
    return df


def get_access_token(client_id, client_secret):
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
    q1 = np.percentile(df[column], 25)
    q3 = np.percentile(df[column], 75)
    return q1, q3


def get_recommendations(token, genre, feature, feature_min, feature_max):
    # Send recommendations request
    endpoint = 'https://api.spotify.com/v1/recommendations?'
    query = f'{endpoint}limit=20&seed_genres={genre}&min_{feature}={feature_min}&max_{feature}={feature_max}'
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

    min_valence, max_valence = compute_quartile(df, 'valence')
    min_dance, max_dance = compute_quartile(df, 'danceability')
    min_energy, max_energy = compute_quartile(df, 'energy')
    token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    get_recommendations(token, 'pop', 'valence', min_valence, max_valence)
    get_recommendations(token, 'pop', 'danceability', min_dance, max_dance)
    get_recommendations(token, 'pop', 'energy', min_energy, max_energy)


if __name__ == "__main__":
    main()
