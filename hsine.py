#!/usr/bin/python
from math import radians, cos, sin, asin, sqrt
import requests, json

# https://github.com/mapado/haversine/blob/master/haversine/haversine.py
# mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
EARTH_RADIUS_KM = 6371.0088
OFFICE = (53.339428, -6.257664)
URL="https://s3.amazonaws.com/intercom-take-home-test/customers.txt"

#Returns dustance in KMs
def get_km(la,lo):

    # unpack latitude/longitude
    lat1, lng1 = OFFICE
    lat2 = float(la)
    lng2 = float(lo)

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

    return int(2 * EARTH_RADIUS_KM * asin(sqrt(d)))

#Returns txt from spoecified URL
def get_file():
    r = requests.get(URL)
    s = r.text
    return s

#Returns list of jsons
def parse_file(j):
    list = []
    for i in j.split('\n'):
        list.append(json.loads(i)) 
    return list

#Sorts filtered guest list
def sort_list(l):
    l.sort(key = lambda x : x["user_id"])
    return l

#Returns sorted by ID and filtered by distance guest list 
def make_glist(l):
    guest_list = []
    for i in range(len(l)):
        km = get_km(l[i]["latitude"],l[i]["longitude"])
        if km <= 100:
            s={"name":l[i]["name"],"user_id":l[i]["user_id"]} #,"K": km}
            guest_list.append(s)
    return sort_list(guest_list)

#Save Glist to output.txt
def save_file(f):
    with open('output.txt','w') as writeme:
        for l in range(len(f)):
            writeme.write('%s\n' % f[l]) 

def main():
    file = get_file()
    list = parse_file(file)
    guest_list = make_glist(list)
    save_file(guest_list)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Sajonara!")
        sys.exit(0)

