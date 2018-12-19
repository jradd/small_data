import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, sys
import json



client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']
uri = 'spotify:track:3j1fOrxmfuym91Cf9v397b'


title = sys.argv[1]
artist = sys.argv[2]
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False



def get_id(artist, title):
  search_query = artist + ' ' + title
  result = sp.search(search_query)
  for i in result['tracks']['items']:
      if (i['artists'][0]['name'] == artist) and (i['name'] == title):
          uri = (i['uri'])
          break
  else:
      try:
          uri = (result['tracks']['items'][0]['uri'])
      except:
          print ("Cannot Find URI")
  return uri



def get_analysis(uri):
  analysis = sp.audio_analysis(uri)
  return analysis

class ExtractValues:
    """Recursively pull values of specified key from nested JSON."""

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key
        self.arr = []
        self.res = self.extract(self.obj, self.arr, self.key)

    @classmethod
    def extract(self, obj, arr, key):
        """Returns all matching values."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    self.extract(v, arr, key)
                elif k == key:
                   arr.append(v)
        elif isinstance(obj, list):
              for item in obj:
                  self.extract(item, arr, key)
        return arr

if __name__ == '__main__':
  artist, title = sys.argv[1], sys.argv[2]
  uri = get_id(artist, title)
  analysis = get_analysis(uri)
  filename = artist + '_' + title + '.json'
  with open(filename, 'wb+') as f:
    f.write(json.dumps(analysis))
    data_read = f.read()
    f.close()
