#!/usr/bin/env python
''' Need to refresh on some 
things to figure out how to 
automate this for plot
not working, but still useful
'''
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

import json
import os



def get_key_names(data):
  data_keys = [x for x in data['sections']]
  return data_keys

def get_segments(data, req):
  reqs = ('timbre', 'pitches', 'start', 'duration')
  for r in reqs:
    if req in reqs:
      segments = [x for x in data['segments']]
      for obj in segments:
        res = [obj[str(req)] for obj in segments]
    print('requested: ', req)
    return res

#  data_keys = get_key_names(data)

#  for obj in segments:
#    timbre = [obj['timbre'] for obj in segments]
#    pitches = [obj['pitches'] for obj in segments]
#    segment_start = [obj['start'] for obj in segments]
#    segment_duration = [obj['duration'] for obj in segments]
#    segment_time = segment_start + segment_duration
    #if obj == [x[obj] for x in data_Keys]:
    #  return obj
    #return (timbre, pitches, segment_start, segment_duration, segment_time)

#  return (timbre, pitches, start)

def get_sections(data, req):
  reqs = (
      'confidence', 'start', 'duration',
      'time_signature', 'tempo', 'mode', 
      'mode_confidence', 'key', 'key_confidence', 
      'loudness', 'loudness_max'
      )
  for r in reqs:
    if r == req:
      sections = [x for x in data['sections']]
      for obj in sections:
        res = [obj[str(req)] for obj in sections]
      for item in res:
        return res

def model_iter(until):
  for n in range(0, until):
    yield n*(n+1)//2
# START BREAKING STUFF WITH MATPLOT

def cc(arg):
  '''
  convert 'named' characters to rgba format with 60% opactiy.
  '''
  return mcolors.to_rgba(arg, alpha=0.6)

#def polygon_under_graph(xlist, ylist):
#  return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]

if __name__ == '__main__':
#  print(get_segments(data))
#  print(get_sections(data))
#  fig = plt.figure()
#  ax = fig.gca(projection='3d')
#
#  verts = []



#  xs = np.linspace(
  filename = 'tt_dram.json'
  data_str = open(filename, 'r').read()
  data = json.loads(data_str)

#  xlist = get_segments(data, 'pitches')
#  ylist = get_sections(data, 'loudness')
  section_start = get_sections(data, 'start')
  section_end   = get_sections(data, 'end')
  segment_start = get_segments(data, 'start')
  segment_end   = get_segments(data, 'duration') + get_segments(data, 'start')

print(sorted(segment_start))
print(sorted(section_start))

