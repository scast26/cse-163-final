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
    artists = '66CXWjxzNUsdJxJ2JdwvnR,3nFkdlSjzX9mRTtwJOzDYB,3TVXtAsR1Inumwj472S9r4'
    tracks = '1CAksvEO6oRHd9bBKWAfuY,1olNHIIVl4EVwIEPGYIR7G,10VBBaul4zVD0reteuIHM2'

    get_artists(token, artists)
    get_tracks(token, tracks)


if __name__ == "__main__":
    main()
