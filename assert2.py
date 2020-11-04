import unittest
#import mylib
import sys
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

   # @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library version")
    #def test_format(self):
        #Tests that work for only a certain version of the library.
     #    pass

    @unittest.skipUnless(sys.platform.startswith("Lin"),
                         "requires Linux")
    def test_windows_support(self):
        # windows specific testing code
        pass