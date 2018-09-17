import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest


os.chdir(os.path.dirname(os.path.abspath(__file__)))
suite = unittest.defaultTestLoader.discover('.')

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
