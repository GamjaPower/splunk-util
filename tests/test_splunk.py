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
import time
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
        for search in searches:
            if search['title'] == 'kpitest2':
                self.manager.del_kpi_base_search(title='kpitest2')

    def test_add_kpi_base_search(self):
        rs = self.manager.add_kpi_base_search(title='kpitest2', desc='test')
        if '_key' in rs:
            self.assertTrue(True)

    def test_get_uuid(self):
        uuids = []
        for x in range(1, 10000):  # @UnusedVariable
            uuids.append(self.manager.get_uuid())
        self.assertEqual(len(uuids), len(list(sorted(set(uuids)))))
        
    def test_get_kpi_services(self):
        for x in self.manager.get_kpi_ids():
            print x

    def test_add_kpi_base_search_metrics(self):
        metrics = []
        metric = {}
        metric['aggregate_statop'] = 'avg'
        metric['entity_statop'] = 'avg'
        metric['threshold_field'] = 'threshold_field'
        metric['title'] = 'threshold_field'
        metric['unit'] = ''
        metric['_key'] = self.manager.get_uuid()
        metrics.append(metric)
        self.manager.add_kpi_base_search_metrics('kpitest2', metrics)
        time.sleep(1)
        for kpi_base_search in self.manager.get_kpi_base_searches():
            if kpi_base_search['title'] == 'kpitest2':
                title = kpi_base_search['metrics'][0]['title']
                self.assertEqual(title, 'threshold_field')
                print kpi_base_search


if __name__ == '__main__':
    unittest.main()
