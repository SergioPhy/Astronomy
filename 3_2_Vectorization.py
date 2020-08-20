#Copy and modify your previous angular_dist and crossmatch in radians functions to calculate the distances to all of the objects in the second catalogue using 
#NumPy arrays.

#The return values should behave the same way as the original function, given the same arguments, except time_taken should be noticeably smaller for large
#catalogues.

# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(ra1,dec1,ra2,dec2): #arguments in radians.
  #r1 = np.radians(ra1)    Discoment if arguments are in degrees
  #d1 = np.radians(dec1)   but change the names of the arguments
  #r2 = np.radians(ra2)    in the equations.
  #d2 = np.radians(dec2)
  a = np.sin( np.abs(dec1-dec2)/2 )**2
  b = np.cos(dec1)*np.cos(dec2)*np.sin( np.abs(ra1-ra2)/2 )**2
  dist = 2*np.arcsin(np.sqrt(a + b))
  return dist

def crossmatch(cat1, cat2, max_radius): #cat1 and cat2 in degrees.
  start = time.perf_counter()
  
  max_radius = np.radians(max_radius)
    
  match = []
  no_match = []
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  ra2s = cat2[:,0]
  dec2s = cat2[:,1]

  
  for id1, (ra1, dec1) in enumerate(cat1):
    dist = angular_dist(ra1, dec1, ra2s, dec2s)
    #min_dist = np.min(dist)
    #min_id = np.argmin(min_dist)
    min_id = np.argmin(dist)
    min_dist = dist[min_id]
    
    if min_dist <= max_radius:
      match.append((id1, min_id, np.degrees(min_dist)))
    else:
      no_match.append(id1)

  time_taken = time.perf_counter() - start     
  return match, no_match, time_taken
