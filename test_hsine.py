#!/usr/bin/python3

from distance import Distance
from hsine import Hsine
from file import File
import unittest
import pathlib as pl

class TestValidator(unittest.TestCase):

    def setUp(self): #__init__(self):
        self.earth = 6371.0088
        self.office = (53.339428, -6.257664)
        self.url1 = "https://pastebin.com/raw/cfA8cxHg" 
        unittest.TestCase.__init__(self)

        self.testLat = [52.1581198,-23.781300385747006,53.33197166003888,53.302452]
        self.testLon = [-7.15054,-45.3963001023727, -6.377250646780829,-6.126921]
        self.result = [int(144.38),int(9367.59),int(7.94),int(9.61)]
        self.name = ["test1","test2","test3","test4"]
        self.user_id = [33,55,77,2]
        self.list = []

        for i in range(len(self.name)):
            s = {"latitude": self.testLat[i], "user_id": self.user_id[i] , "name": self.name[i], "longitude": self.testLon[i]}
            self.list.append(s)

    #Testing haversine formula 
    def test_a_distance(self):
        a = Distance(self.earth, self.office)

        for i in range(len(self.result)):
            distance = a.get_km(self.testLat[i],self.testLon[i])
            self.assertEqual(distance,self.result[i])
        print('DISTANCE TESTS PASSED')

    #Testing Guest List filtering function
    def test_b_guestlist(self):
        a = Distance(self.earth, self.office)
        b = Hsine(self.earth, self.office,"url") 
        mkgl = b.make_glist(a,self.list)

        #user_id's 2 and 77 should appeared in sorted list ascendingly
        self.assertEqual(mkgl[0]["user_id"],2)
        self.assertEqual(mkgl[1]["user_id"],77)
        #there are 2 results filing "within 100KM" criterium
        self.assertEqual(len(mkgl),2)
        print('GLIST FILTERING and SORTING TESTS PASSED')


    #Pastebin link with "This is test!" text > verifies if it was correctly parsed 
    def test_c_url(self):
        u = File(self.url1)
        t = u.get_file()
        self.assertEqual(t,"This is test!")
        print("URL TEXT PARSING TESTS PASSED")

    #https://stackoverflow.com/questions/59121161/python-unittest-how-to-assert-the-existence-of-a-file-or-folder-and-print-the-p/59198749#59198749
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_d_filesave(self):
        h = Hsine(self.earth, self.office,"url")
        h.save_file(self.list)
        cwd = pl.Path.cwd()
        path = str(cwd) + "/output.txt"
        self.assertIsFile(path)
        print("SAVE FILE TEST PASSED")


if __name__ == '__main__':
    unittest.main(verbosity=2)
