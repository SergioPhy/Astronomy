#Copy crossmatch from Break out and modify it to only loop through objects in the second catalogue with declinations between dec1 - max_radius and 
#dec1 + max_radius using binary search.

#Your crossmatch should use np.searchsorted to find the starting point (just before dec1 - max_radius) and then break out of the loop when the 
#declination reaches dec1 + max_radius.

#The return values should behave the same way as the original function, given the same arguments, except time_taken should be noticeably smaller for 
#large catalogues.

#Hint
#Don't forget to use np.searchsorted to find the start and end indices of the loop through the declination-sorted second catalogue after you've sorted it.

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
  
  #Looping cat1
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id = None
    
    #Conditions
    min_dec = dec1 - max_radius
    max_dec = dec1 + max_radius
    
    #Finding the id of the start and end in the cat2_ordered for declinations
    start = np.searchsorted(cat2_ordered[:,1], min_dec, side='left')
    end = np.searchsorted(cat2_ordered[:,1], max_dec, side='right')
    
    #Looping cat2 in within the limits of start and end
    for id2, (ra2, dec2) in enumerate(cat2_ordered[start:end], start):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      
      if dist<min_dist:
        min_dist = dist      #these two steps are very interesting
        min_id = order[id2]  #real id (of the origianl array cat2)
        
    if min_dist <= max_radius:
      match.append((id1, min_id, min_dist))
    else:
      no_match.append(id1)
      
  time_taken = time.perf_counter() - start
  
  return match, no_match, time_taken
