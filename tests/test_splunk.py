# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 12.
@author: jason96
'''

import unittest

from splunklib.client import Index
from sputil.splunk import Indexer, Searcher, ITSIManager
from sputil.base import SPINDEX

import urllib3
urllib3.disable_warnings()


class SplunkIndexerTest(unittest.TestCase):

    def setUp(self):
        self.indexer = Indexer()

    def tearDown(self):
        pass

    def test_index(self):
        json_string = '{"spindex":"test"}'
        i = self.indexer.index(SPINDEX, json_string)
        self.assertEqual(Index, type(i))


class SplunkSearcherTest(unittest.TestCase):

    def setUp(self):
        self.searcher = Searcher()

    def tearDown(self):
        pass

    def test_search(self):
        spl = ' search index=_internal | head 10  '
        for x in self.searcher.search(spl):
            self.assertEqual('_internal', x['index'])


class ITSIManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = ITSIManager()

    def test_get_kpi_base_searches(self):
        searches = self.manager.get_kpi_base_searches()
        self.assertGreater(len(searches), 0)

    def test_add_kpi_base_search(self):
        rs = self.manager.add_kpi_base_search(title='test2', desc='test')
        if '_key' in rs:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
