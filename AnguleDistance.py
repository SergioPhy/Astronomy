Write a function called angular_dist that calculates the angular distance between any two points on the celestial sphere given their right ascension and declination.

Your function should take arguments in decimal degrees and return the distance in decimal degrees too.

import numpy as np

# Write your angular_dist function here.

def angular_dist(ra1,dec1,ra2,dec2):
  r1 = np.radians(ra1)
  d1 = np.radians(dec1)
  r2 = np.radians(ra2)
  d2 = np.radians(dec2)
  
  a = np.sin( np.abs(d1-d2)/2 )**2
  b = np.cos(d1)*np.cos(d2)*np.sin( np.abs(r1-r2)/2 )**2
  dis = 2*np.arcsin(np.sqrt(a + b))
  
  return np.degrees(dis)
