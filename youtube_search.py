#!/usr/bin/env python
''' 
Search Youtube for a given keyword and return content details up to
a maximum count.
'''

from __future__ import print_function

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import os
import json, csv

# Set GOOGLE_API_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class YoutubeData:
  def __init__(self):
    self.api_key = os.environ['GOOGLE_API_KEY']
    self.youtube_api_service_name = 'youtube'
    self.youtube_api_version = 'v3'


  def youtube_client(self):
    client = build(self.youtube_api_service_name, self.youtube_api_version, developerKey=self.api_key)
    return client

  def youtube_search(self, options):
    search_response = self.youtube_client().search().list(
        q=options.q,
        part='id,snippet',
        order='date',
        maxResults=options.max_results
    ).execute()

    titles   = []
    videoIds = []
    
    for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        titles.append(search_result['snippet']['title'])
        videoIds.append(search_result['id']['videoId'])
    return videoIds

  def youtube_video_details( self, video_ids ):
    video_details = self.youtube_client().videos().list(
        part = 'snippet,contentDetails,statistics',
        id = ','.join(video_ids)
        ).execute()

    return video_details

  def youtube_data(self, data, dict_check, dict_push):
    if data in dict_check:
      if isinstance(dict_check[data], list):
        dict_check[data] = ', '.join(dict_check[data])
      dict_push[data] = dict_check[data]
      


if __name__ == '__main__':
  data_flow = YoutubeData()
  video_description = {}
  
  argparser.add_argument('--q', help='Search term', default='Google')
  argparser.add_argument('--max-results', help='Max results', default=25)
  args = argparser.parse_args()

  
  try:
    video_ids = data_flow.youtube_search(args)
    if video_ids:
      for video_id in video_ids:
        video_description[video_id] = {}
        video_details = data_flow.youtube_video_details(video_ids)
        for video_detail in video_details['items']:
          videoDetails =  video_description[video_id][video_detail['id']] = {}
          title    = data_flow.youtube_data('title', video_detail['snippet'], video_description[video_id][video_detail['id']])
          date_pub = data_flow.youtube_data('publishedAt', video_detail['snippet'], video_description[video_id][video_detail['id']])
          duration = data_flow.youtube_data('duration', video_detail['contentDetails'], video_description[video_id][video_detail['id']])
          likes    = data_flow.youtube_data('likes', video_detail['statistics'], video_description[video_id][video_detail['id']])
          comments = data_flow.youtube_data('commentCount', video_detail['statistics'], video_description[video_id][video_detail['id']])
          views    = data_flow.youtube_data('viewCount', video_detail['statistics'], video_description[video_id][video_detail['id']])
       # print({videoDetails: duration})
        

        print(sorted(video_description.items()))

      with open('youtube_video_details.json', 'w') as fp:
        fp.write(json.dumps(video_description, sort_keys=True, indent=4, separators=(',', ': ')))
        fp.close()

  except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
