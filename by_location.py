from p1 import *
import pyglet
import geoplotlib
from geoplotlib.utils import read_csv

df = read_csv("Reviews2 .csv")  #replace path with your file path
geoplotlib.dot(df)
geoplotlib.show()
