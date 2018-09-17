# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 17.

@author: jason96
'''
import json
import requests


# url = 'https://127.0.0.1:8089/servicesNS/nobody/SA-ITOA/' + \
#     'itoa_interface/kpi_base_search'
# req = requests.get(url, auth=('admin', 'changepassword'), verify=False)
# print json.loads(req.content)

url = 'https://127.0.0.1:8089/servicesNS/nobody/SA-ITOA/' + \
    'itoa_interface/kpi_base_search'


kpi_base_search = {}
kpi_base_search['title'] = 'title2'
kpi_base_search['description'] = 'title2'


req = requests.post(url, auth=('admin', 'changepassword'),
                    data=json.dumps(kpi_base_search),
                    verify=False)
print json.loads(req.content)
