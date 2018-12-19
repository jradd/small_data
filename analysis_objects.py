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
import matplotlib as mlab
import json
import os
import pickle



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

def scatterplot(x_data, y_data, x_label, y_label, title):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Call the function to create plot
def histogram(data, x_label, y_label, title):
    _, ax = plt.subplots()
    ax.hist(data, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

def get_colors(inp, colormap, vmin=None, vmax=None):
    norm = plt.Normalize(vmin, vmax)
    return colormap(norm(inp))


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

  segment_pitches  = get_segments(data, 'pitches')
  segment_start = get_segments(data, 'start')
  segment_duration   = get_segments(data, 'duration')
  segment_timbre = get_segments(data, 'timbre')

  section_start = get_sections(data, 'start')
  section_duration = get_sections(data, 'duration')
  section_confidence = get_sections(data, 'confidence')
  section_time_signature = get_sections(data, 'time_signature')
  section_tempo = get_sections(data, 'tempo')
  section_mode = get_sections(data, 'mode')
  section_loudness = get_sections(data, 'loudness')
#  section_loudness_max = get_sections(data, 'loudness_max')
  section_key = get_sections(data, 'key')
  
  x = np.array(segment_pitches)
  zx = np.array(segment_timbre)
  xlist = np.sort(np.array(segment_start))
  xlist2 = np.sort(np.array(section_start))
  y  = np.array(section_key)
  yz = np.array(segment_duration)
  xz = np.array(section_duration)
  Z = (np.cos(x*0.2) + np.sin(zx*0.3))
  Zpos = np.ma.masked_less(Z, 0)
  Zneg = np.ma.masked_greater(Z, 0)

  cmap = {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
  cdict = {'red':   [(0.0,  0.0, 0.0),
                     (0.5,  1.0, 1.0),
                     (1.0,  1.0, 1.0)],

           'green': [(0.0,  0.0, 0.0),
                     (0.25, 0.0, 0.0),
                     (0.75, 1.0, 1.0),
                     (1.0,  1.0, 1.0)],

           'blue':  [(0.0,  0.0, 0.0),
                     (0.5,  0.0, 0.0),
                     (1.0,  1.0, 1.0)]}
  r = [i for i in range(0, len(xlist))]
  plt.plot(xlist, x, xlist2, y)
  plt.show()
#  fig.colorbar(pos, ax=ax1)
#  neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')
#  fig.colorbar(neg, ax=ax2)
#  plt.show()
#  plt.scatter(xlist2, y, cmap=colors)
#  plt.show()
 # plt.plot(xlist, yz)
#  plt.quiver(xlist2, y, x, zx)
##  plt.plot(xlist, r, 'g^', xlist2, y, 'g-')
#  plt.hist2d(xlist, x)

##### On to something here.
#  for i in range(section_len):
#    xlist2.append((([0] * i) + xlist[i:i+1] + ([0] * (len(xlist) - 1 - i)))[:len(xlist)])
#  print(xlist2)

#  pobject = zip(x, zx, y, xlist, xlist2)
#  plt.plot(xlist, x, 'ro')
#  plt.axis([0,300,0, 300])
#  plt.show()
