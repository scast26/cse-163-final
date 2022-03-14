from main import (requests, json,
                  get_access_token, CLIENT_ID, CLIENT_SECRET)


def get_artists(token, artists):
    endpoint = f'https://api.spotify.com/v1/artists?ids={artists}'
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    res = requests.get(endpoint, headers=header)
    artists = res.json()
    with open('artist_score_validation.txt', 'w') as t:
        for i in artists['artists']:
            t.write(f"The artist '{i['name']}' has a" +
                    f" popularity score of {i['popularity']}")
            t.write('\n')
    with open('artist_score_validation.json', 'w') as j:
        json.dump(artists, j, indent=2)


def get_tracks(token, tracks):
    endpoint = f'https://api.spotify.com/v1/tracks?ids={tracks}'
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    res = requests.get(endpoint, headers=header)
    tracks = res.json()
    with open('track_score_validation.txt', 'w') as t:
        for i in tracks['tracks']:
            t.write(f"The song '{i['name']}' by " +
                    f"{i['artists'][0]['name']} has a" +
                    f" popularity score of {i['popularity']}")
            t.write('\n')
    with open('track_score_validation.json', 'w') as j:
        json.dump(tracks, j, indent=2)


def main():
    token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    artists = '3Nrfpe0tUJi4K4DXYWgMUX,66CXWjxzNUsdJxJ2JdwvnR,' +\
              '3TVXtAsR1Inumwj472S9r4,6jJ0s89eD6GaHleKKya26X'
    tracks = '03iCbZaM4OkRR4We6wIzvx,7l94dyN2hX9c6wWcZQuOGJ,' +\
             '6V2D8Lls36APk0THDjBDfE,4r6eNCsrZnQWJzzvFh4nlg'

    get_artists(token, artists)
    get_tracks(token, tracks)


if __name__ == "__main__":
    main()
