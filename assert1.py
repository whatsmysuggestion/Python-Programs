import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('kka'.upper(), 'KKAR')
    def test_isupper(self):
        self.assertTrue('KKAR'.isupper())
        self.assertFalse('KKAR'.islower())
    def test_split(self):
        s = 'Kkar:technologies'
        self.assertEqual(s.split(":"), ['Kkar', 'technologies'])


