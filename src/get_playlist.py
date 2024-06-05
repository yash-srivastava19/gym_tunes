import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

def get_random_playlist(query, client_id, client_secret, limit=10):
    # Initialize Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Search for playlists based on the query
    results = sp.search(q=query, type='playlist', limit=limit)
    
    # Extract playlists from the results
    playlists = results['playlists']['items']
    
    # If no playlists found, return None
    if not playlists:
        return None
    
    # Choose a random playlist
    random_playlist = random.choice(playlists)
    
    # Extract relevant information
    playlist_name = random_playlist['name']
    playlist_link = random_playlist['external_urls']['spotify']
    
    return playlist_name, playlist_link

"""
# Example usage
query = 'summer 2024 vibes'  # You can change this to any genre, mood, or keyword
result = get_random_playlist(query)

if result:
    name, link = result
    print(f"Random playlist: {name}")
    print(f"Link: {link}")
else:
    print("No playlists found for the given query.")

"""