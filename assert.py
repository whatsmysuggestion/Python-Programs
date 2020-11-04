import unittest

class TestStringMethods(unittest.TestCase):


    def multiplication(self,a,b):
        return(a*b)

    def testmycode(self):
        res=self.multiplication(10,3)
        self.assertEqual(30,res)

    def testmycode1(self):

        if (self.multiplication(2, 3) == 5):
            res = True
        else:
            res = False
        self.assertTrue(res)

