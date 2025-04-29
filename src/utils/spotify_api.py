import requests

def get_spotify_data(endpoint, headers):
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from Spotify API: {response.status_code}")

def authenticate_spotify(client_id, client_secret):
    auth_url = "https://accounts.spotify.com/api/token"
    payload = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_url, data=payload, auth=(client_id, client_secret))
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Error authenticating with Spotify API: {response.status_code}")

def search_track(track_name, access_token):
    endpoint = f"https://api.spotify.com/v1/search?q={track_name}&type=track"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    return get_spotify_data(endpoint, headers)