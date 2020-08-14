#Write import_bss and import_super functions that import the AT20G BSS and SuperCOSMOS catalogues from the files bss.dat and super.csv as described in the previous slides.

#Each function should return a list of tuples containing the object's ID (an integer) and the coordinates in degrees. The object ID should be the row of the object in the catalogue, starting at 1.

import numpy as np

# Write your import_bss function here.
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
