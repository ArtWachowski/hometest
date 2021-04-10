#!/usr/bin/python
from distance import Distance
from file import File
#import json

# mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
EARTH = 6371.0088
OFFICE = (53.339428, -6.257664)
URL="https://s3.amazonaws.com/intercom-take-home-test/customers.txt"

#Sorts filtered guest list
def sort_list(l):
    l.sort(key = lambda x : x["user_id"])
    return l

#Returns sorted by ID and filtered by distance guest list 
def make_glist(k,l):
    guest_list = []
    for i in range(len(l)):
        km = k.get_km(l[i]["latitude"],l[i]["longitude"])
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
    k = Distance(EARTH,OFFICE) 
    f = File(URL)
    list = f.parse_file()
    guest_list = make_glist(k,list)
    save_file(guest_list)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Sajonara!")
        sys.exit(0)

