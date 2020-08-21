 #Copy your crossmatch solution from Microoptimisation and modify it so that it sorts catalogue 2 by declination and breaks out of the inner loop early.

#Your crossmatch should break out of the loop over the second catalogue when the declination reaches dec1 + max_radius.

#The return values should behave the same way as the original function, given the same arguments, except time_taken should be noticeably smaller for 
#large catalogues.

# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(ra1,dec1,ra2,dec2): #radians
  
  a = np.sin( np.abs(dec1-dec2)/2 )**2
  b = np.cos(dec1)*np.cos(dec2)*np.sin( np.abs(ra1-ra2)/2 )**2
  dist = 2*np.arcsin(np.sqrt(a + b))
  
  return dist

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  max_radius = np.radians(max_radius)
  
  #Ordering the cat2 by its declination
  order = np.argsort(cat2[:,1]) #these steps are very interesting
  cat2_ordered = cat2[order]
  #print(cat2_ordered)
  
  match = []
  no_match = []
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id = None
    max_dec = dec1 + max_radius
    
    for id2, (ra2, dec2) in enumerate(cat2_ordered):
      if dec2 > max_dec:
        break
      
      dist = angular_dist(ra1, dec1, ra2, dec2)
      
      if dist<min_dist:
        min_dist = dist      #these two steps are very interesting
        min_id = order[id2]
        
    if min_dist <= max_radius:
      match.append((id1, min_id, min_dist))
    else:
      no_match.append(id1)
      
  time_taken = time.perf_counter() - start
  
  return match, no_match, time_taken
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
