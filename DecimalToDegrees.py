#Write two functions, one that converts right ascension from HMS to decimal degrees, called hms2dec, and another that converts declination from DMS to decimal degrees, called dms2dec.

#Right ascension is always an angle from 0 to 24 hours and declination is always an angle from -90° to +90°.

# Write your hms2dec and dms2dec functions here
def hms2dec(h,m,s):
  r_a = 15*(h + m/60 + s/3600)
  return r_a

def dms2dec(d,m,s):
  dec = abs(d) + m/60 + s/3600
  if d<0: dec = -dec
    
  return dec
