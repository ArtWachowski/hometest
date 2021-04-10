import requests, json

#Parses file from URL and returns list 
class File:

    def __init__(self, url):
        self.url = url

    #Returns txt from URL
    def get_file(self):
        r = requests.get(self.url)
        s = r.text
        return s

    #Returns list of jsons
    def parse_file(self):
        j = self.get_file()
        list = []
        for i in j.split('\n'):
            list.append(json.loads(i)) 
        return list
