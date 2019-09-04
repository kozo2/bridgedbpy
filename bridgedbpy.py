import requests
import re

__author__ = 'Kozo Nishida'
__email__ = 'knishida@riken.jp'
__version__ = '0.0.1'
__license__ = 'MIT'

API_BASE = 'https://webservice.bridgedb.org/'

def hmdb2kegg(hmdb_id):
    req = requests.get(API_BASE + 'Human/xrefs/Ch/' + hmdb_id + '?dataSource=Ck')
    if req.status_code == 200:
        return re.findall(rb'C[0-9]{5}', req.content)
    else:
        print("Request failed for " + hmdb_id)
