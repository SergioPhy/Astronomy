#Write a crossmatch function for two catalogues to within a maximum radius. The catalogues are 2D NumPy arrays of RA and declination in degrees.

#Your function should convert all the coordinates to radians before it starts crossmatching. It should return 3 values:

#A list of tuples of matched IDs and their distance in degrees;
#A list of unmatched IDs from the first catalogue;
#The time taken (in seconds) to run the crossmatcher.
#Both catalogues are given as an N×2 NumPy array of floats. Each row contains the coordinates of a single object. The two columns are the RA and declination.

#An object's ID is the index of its row, starting at 0. Your function should work with input catalogues with any number of objects.

# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(ra1,dec1,ra2,dec2): #radians
  
  a = np.sin( np.abs(dec1-dec2)/2 )**2
  b = np.cos(dec1)*np.cos(dec2)*np.sin( np.abs(ra1-ra2)/2 )**2
  dist = 2*np.arcsin(np.sqrt(a + b))
  
  return np.degrees(dist)

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  
  cat1_rad = []
  cat2_rad = []
  
  for i, row in enumerate(cat1, 0):
    cat1_rad.append((i, np.radians(row[0]), np.radians(row[1])))
  
  for i, row in enumerate(cat2, 0):
    cat2_rad.append((i, np.radians(row[0]), np.radians(row[1])))
  
  match = []
  no_match = []
  max_radius = max_radius
  
  for id1, ra1, dec1 in cat1_rad:
    closest_dist = np.inf
    closest_id = None
    
    for id2, ra2, dec2 in cat2_rad:
      dist = angular_dist(ra1, dec1, ra2, dec2)
      
      if dist < closest_dist:
        closest_dist = dist
        closest_id = id2
    
    if closest_dist <= max_radius:
      match.append((id1, closest_id, closest_dist))
    else:
      no_match.append(id1)
      
  time_taken = time.perf_counter() - start
  
  return match, no_match, time_taken
