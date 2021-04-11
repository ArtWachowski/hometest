import sys, requests, json

#Parses file from URL and returns list 
class File:

    def __init__(self, url):
        self.url = url

    #Returns txt from URL
    def get_file(self):

        r = requests.get(self.url)

        if r.status_code != 200:
            raise Exception('URL is not accesible!')
            sys.exit(0)

        s = r.text
        return s

    #Returns jsons
    def parse_file(self):
        j = self.get_file()
        list = []
        #TODO Validate input
        for i in j.split('\n'):
            list.append(json.loads(i)) 
        return list
