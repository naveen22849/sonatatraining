import unittest
from day2.larUsing_Fn  import*
class largestTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(largestnumber(100,20,30),"number 1 is large")

    def test2(self):
        self.assertEqual(largestnumber(1,20,3),"number 2 is large")

    def test3(self):
        self.assertEqual(largestnumber(1,2,3),"number 3 is large")

    def test4(self):
        self.assertNotEqual(largestnumber(1,2,"nave"),"please enter a valid input")

    @classmethod
    def setUpClass(self):
        print("setup class")

    @classmethod
    def tearDownClass(self):
        print("teardown class")