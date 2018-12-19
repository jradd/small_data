from __future__ import print_function
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys, os
import json

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']
#uri = 'spotify:track:0BCPKOYdS2jbQ8iyB56Zns'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
#features = sp.audio_features(uri)
#print ('Energy:', features[0]['energy'])
#print ('Calence:', features[0]['valence'])

def get_id(title, artist):
  search_str = title + ' ' + artist
  result     = sp.search(search_str)
  for i in result['tracks']['items']:
    uri = i['uri']
#    if (i['artists'][0]['name'] == artist) and (i['name'] == title):
    m = f'{artist} - {title}'
    out = f'{uri}'
    return out


    if feats:
      return feats
  return features


title, artist = sys.argv[1], sys.argv[2]
uri = get_id(title, artist)
features = sp.audio_features(uri)
filename = artist + '_' + title + '.features'
with open(filename, 'w+') as f:
  data = f.write(json.dumps(features, indent=4))
  data_read = f.read()
  f.close()
print(f'{title} - {artist} - {uri}')
feats = ('energy', 'valence', 'speechiness', 'danceability', 'key', 'loudness', 'mode', 'acousticness', 'instrumentalness', 'liveness', 'tempo', 'duration_ms', 'time_signature')
for i in features:
  energy =  i['energy']
  valence =  i['valence']
  speechiness =  i['speechiness']
  danceability =  i['danceability']
  key = i['key']
  loudness = i['loudness']
  mode = i['mode']
  acousticness = i['acousticness']
  instrumentalness = i['instrumentalness']
  liveness = i['liveness']
  tempo    = i['tempo']
  duration_ms = i['duration_ms']
  time_signature = i['time_signature']
  for feat in feats:
    print(f'{feat}',i[feat])
