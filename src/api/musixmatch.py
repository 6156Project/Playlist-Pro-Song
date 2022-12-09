import requests
import os

class Musixmatch():
  def __init__(self, config_info) -> None:
    self.key = config_info.key

  def get_songs(self, req_args):
    rsp = ""
    try:
      if not req_args or 'song_name' not in req_args or len(req_args['song_name']) == 0:
        rsp = "Search field empty."
      else:
        page = req_args['page'] if 'page' in req_args else 1
        page_size = req_args['page_size'] if 'page_size' in req_args else 10
        rsp = requests.get(
          'http://api.musixmatch.com/ws/1.1/track.search',
          params={
            'apikey': self.key,
            'q_track': req_args['song_name'],
            'page': page,
            'page_size': page_size
          }
        )
        rsp = rsp.json()
        rsp = self.clean_song_response(rsp['message']['body']['track_list'])
      
    except:
      print('ehh, this isnt suppose to happen')

    return rsp

  def clean_song_response(self, song_list):
    songs = []
    for s in song_list:
      song = {}
      song['song_id'] = s['track']['track_id']
      song['song_name'] = s['track']['track_name']
      song['album_id'] = s['track']['album_id']
      song['album_name'] = s['track']['album_name']
      song['artist_id'] = s['track']['artist_id']
      song['artist_name'] = s['track']['artist_name']
      songs.append(song)
    return songs