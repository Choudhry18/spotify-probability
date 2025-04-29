import json
from collections import Counter
import numpy as np
from scipy.stats import nbinom

def analyze_streaming_data(streaming_data, wrapped_data):
    # Extract the top track URI from wrapped data
    top_track_uri = wrapped_data['topTracks']['topTracks'][0]

    # Count occurrences of each track in streaming history
    shuffle_track_uris = [
        entry['spotify_track_uri']
        for entry in streaming_data
        if entry["reason_start"] in set(["trackdone", "fwdbtn"]) and entry["shuffle"]
    ]

    track_counts = Counter(shuffle_track_uris)
    total_tracks_played = len(shuffle_track_uris)

    # Estimate p = probability of hearing the top track in any given play
    top_track_actual_plays = track_counts.get(top_track_uri, 0)
    p = top_track_actual_plays / total_tracks_played

    # Expected number of plays until hearing top track
    expected_plays = 1 / p if p > 0 else float('inf')

    return {
        "total_tracks_played": total_tracks_played,
        "top_track_actual_plays": top_track_actual_plays,
        "estimated_probability": p,
        "expected_plays": expected_plays
    }