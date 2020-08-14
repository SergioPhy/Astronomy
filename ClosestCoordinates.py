#Write a find_closest function that takes a catalogue and the position of a target source (a right ascension and declination) and finds the closest match for the target source in the catalogue.

#Your function should return the ID of the closest object and the distance to that object.

#The right ascension and declination are in degrees. The catalogue list has been loaded by import_bss from the previous question. The full 320 object BSS catalogue is contained in bss.dat for you to test your code on.

# Write your find_closest function here
import numpy as np

def hms2dec(h,m,s):
  r_a = 15*(h + m/60 + s/3600)
  return r_a

def dms2dec(d,m,s):
  dec = abs(d) + m/60 + s/3600
  sign = d/abs(d)
  return sign*dec

def import_bss():
  data = np.loadtxt('bss.dat', usecols=range(1,7))
  res = []
  
  for i, row in enumerate(data, 1):
    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  
  return res

def angular_dist(ra1,dec1,ra2,dec2):
  r1 = np.radians(ra1)
  d1 = np.radians(dec1)
  r2 = np.radians(ra2)
  d2 = np.radians(dec2)
  
  a = np.sin( np.abs(d1-d2)/2 )**2
  b = np.cos(d1)*np.cos(d2)*np.sin( np.abs(r1-r2)/2 )**2
  dist = 2*np.arcsin(np.sqrt(a + b))
  
  return np.degrees(dist)

def find_closest(cat,ra,dec): #cat has 3 dimensions
  min_dist = np.inf
  min_id = None
  for id1, ra1, dec1 in cat:
    dist = angular_dist(ra1, dec1, ra, dec)
    
    if dist < min_dist:
      min_dist = dist
      min_id = id1
  
  return min_id, min_dist
