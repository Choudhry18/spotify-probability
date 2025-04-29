import json

def load_streaming_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_top_track(data):
    top_track_uri = data['topTracks']['topTracks'][0]
    return top_track_uri

def count_track_occurrences(streaming_data):
    from collections import Counter
    shuffle_track_uris = [
        entry['spotify_track_uri']
        for entry in streaming_data
        if entry["reason_start"] in set(["trackdone", "fwdbtn"]) and entry["shuffle"]
    ]
    track_counts = Counter(shuffle_track_uris)
    return track_counts

def calculate_probability(track_counts, top_track_uri):
    total_tracks_played = sum(track_counts.values())
    top_track_actual_plays = track_counts.get(top_track_uri, 0)
    p = top_track_actual_plays / total_tracks_played if total_tracks_played > 0 else 0
    return p, total_tracks_played, top_track_actual_plays

def expected_plays_until_top_track(p):
    r = 1  # waiting for the first success
    expected_plays = r / p if p > 0 else float('inf')
    return expected_plays