from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import \
    FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
import io
from PIL import Image


def mplimage(request):
  fig = Figure()
  canvas  = FigureCanvas(fig)
  ax = fig.add_subplot(111)
  x = np.arange(-4, 0.5, .02)
  y = np.sin(np.exp(2*x))
  ax.plot(x, y)
  s = io.StringIO()
  response = HttpResponse(s.getvalue(), content_type='image/jpg')
  canvas.print_jpg(response)
  return response
