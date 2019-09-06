import requests
import re

__author__ = 'Kozo Nishida'
__email__ = 'knishida@riken.jp'
__version__ = '0.0.1'
__license__ = 'MIT'

API_BASE = 'https://webservice.bridgedb.org/'

SYSTEM_CODE = dict([('HMDB', 'Ch'), ('ChEBI', 'Ce'), ('PubChem-compound', 'Cpc')])

def hmdb2kegg(hmdb_id):
    req = requests.get(API_BASE + 'Human/xrefs/Ch/' + hmdb_id + '?dataSource=Ck')
    if req.status_code == 200:
        cids = re.findall(rb'C[0-9]{5}', req.content)
        return [cid.decode("utf-8") for cid in cids]
    else:
        print("Request failed for " + hmdb_id)

def gpml2kegg(database, xrefid):
    if database in SYSTEM_CODE.keys():
        req = requests.get(API_BASE + 'Human/xrefs/' + SYSTEM_CODE[database] + '/' + xrefid + '?dataSource=Ck')
        if req.status_code == 200:
            cids = re.findall(rb'C[0-9]{5}', req.content)
            return " ".join([cid.decode("utf-8") for cid in cids])
    else:
        print(database + "is not in SYSTEM_CODE")
    