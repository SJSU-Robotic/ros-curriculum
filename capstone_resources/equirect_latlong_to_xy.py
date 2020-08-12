#!/usr/bin/env python
from math import radians, cos

# constants w.r.t Mars Society MDRS
R     =  6378137.0      # earth equatorial radius, in meters
lat1  =       38.406419 # initial latitude
long0 =     -110.791920 # initial longitude

# converts input latitude and longitude coordinates 
#   (expressed as degrees!)
# into ROS x, y w.r.t /map coordinates
def equirect_latlong_to_xy(lat, long):
  global R, lat1, long0
  x = R * (radians(long) - radians(long0)) * cos(radians(lat1))
  y = R * (radians(lat) - radians(lat1))
  return x,y