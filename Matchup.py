#Write a crossmatch function that crossmatches two catalogues within a maximum distance. It should return a list of matches and non-matches for the first 
catalogue against the second.

#The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object 
IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs.

#The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you’ve seen previously. The maximum distance is given in decimal 
degrees.

# Write your crossmatch function here.
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

def import_super():
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0,1])
  res = []
  
  for i, row in enumerate(data, 1):
    res.append((i, row[0], row[1]))
  
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

def crossmatch(cat1, cat2, max_radius):
  match = []
  no_match = []  
  
  for id1, ra1, dec1 in cat1:
    closest_dist = np.inf
    closest_id = None
    
    for id2, ra2, dec2 in cat2:
      dist = angular_dist(ra1, dec1, ra2, dec2)
      
      if dist < closest_dist:
        closest_dist = dist
        closest_id = id2
    
    if closest_dist <= max_radius:
      match.append((id1, closest_id, closest_dist))
    else:
      no_match.append(id1)

  return match, no_match
