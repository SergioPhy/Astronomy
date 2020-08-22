#The SkyCoord objects are general purpose sky catalogue storage and manipulation objects in Astropy. 
#They take anything that looks like an array of coordinates as long as you specify the units (here we specify degrees with u.degree) 
#and a reference frame (ICRS is essentially the same as equatorial coordinates. The outputs, closest_id and closest_dists give the 
#matching object's row index in sky_cat2 and the distance to it. closest_dists is the angular distance while closest_dists3d is the 
#3D distance which we're not concerned with here.

#Note
#Astropy returns distances as Quantity objects. You can convert these to NumPy arrays by accessing their value attribute like this:
#closest_dists_array = closest_dists.value

#Copy your crossmatch solution from Microoptimisation and (substantially!) modify it to use Astropy to perform the matching.

#The return values should behave the same way as the original function, given the same arguments, except time_taken should 
#be noticeably smaller for large catalogues.

#Hint
#Astropy doesn't let you specify a maximum radius, so you'll have to weed out matches with distances greater than 5 degrees yourself.


# Write your crossmatch function here.
from astropy.coordinates import SkyCoord
from astropy import units as u
import time
import numpy as np

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  sky_cat1 = SkyCoord(cat1*u.degree, frame='icrs')
  sky_cat2 = SkyCoord(cat2*u.degree, frame='icrs')
  #print(sky_cat1)
  
  #closest_ids is already an array, whereas closest_dists is not
  closest_ids, closest_dists, _ = sky_cat1.match_to_catalog_sky(sky_cat2)
  #print(closest_ids)
  #print(closest_dists.value)
  
  closest_dists_array = closest_dists.value
  match = []
  no_match = []
  
  #Putting together the arrays and convert them in an array
  data = zip(closest_ids, closest_dists_array)
  data = list(data)
  #print(data)
  
  for id1, (closest_id2, dist) in enumerate(data):
    if dist < max_radius:
      match.append((id1, closest_id2, dist))
    else:
      no_match.append(id1)
    
  time_taken = time.perf_counter() - start
  return match, no_match, time_taken
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
