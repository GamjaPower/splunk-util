# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 12.
@author: jason96
'''

import unittest
from sputil.base import SplunkBase


class SplunkBaseTest(unittest.TestCase):

    def setUp(self):
        self.base = SplunkBase()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.base.config['splunk_ip'], '127.0.0.1')
        self.assertGreater(len(self.base.service.apps), 0)
        self.assertGreater(len(self.base.service.indexes), 0)


if __name__ == '__main__':
    unittest.main()
