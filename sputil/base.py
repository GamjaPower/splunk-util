# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 12.
@author: jason96
'''

import ConfigParser
from splunklib import client


SPINDEX = 'sputil-test'


class SplunkBase(object):

    def __init__(self):
        cfg = ConfigParser.ConfigParser()
        cfg.read('splunk.cfg')
        self.config = {}
        self.config['splunk_ip'] = cfg.get('splunk', 'ip')
        self.config['splunk_id'] = cfg.get('splunk', 'id')
        self.config['splunk_port'] = cfg.get('splunk', 'port')
        self.config['splunk_password'] = cfg.get('splunk', 'password')

        self.service = client.connect(host=self.config['splunk_ip'],
                                      port=self.config['splunk_port'],
                                      username=self.config['splunk_id'],
                                      password=self.config['splunk_password'])


class SplunkCustom(SplunkBase):

    def __init__(self):
        super(SplunkCustom, self).__init__()
