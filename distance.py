import math

def dist(lat1, lon1, lat2, lon2):
   R = 6371  # radius of Earth in kilometers
   dlat = math.radians(lat2 - lat1)  # convert latitude difference to radians
   dlon = math.radians(lon2 - lon1)  # convert longitude difference to radians
   
   # calculate part of the haversine formula
   a = math.sin(dlat/2)**2 + \
       math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
   
   # calculate the final distance
   return 2 * R * math.asin(math.sqrt(a))  # return distance in kilometers