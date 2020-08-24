# --------------------------------------------------------
# Author: SamiHei
#
# Python Library for Web API Request
#
# DOCS:
#    - https://requests.readthedocs.io/en/master/
# --------------------------------------------------------

import requests

'''
Simple GET requets

Arguments:
   - url = Target endpoint url

Returns:
   - (HTTP status code, Content-type, text)
'''
def get_request(url):
    req = requests.get(url)
    answer = (req.status_code, req.headers['content-type'], req.text)
    return answer

