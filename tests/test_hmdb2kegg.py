import pytest
from bridgedbpy import *

def test_hmdb2kegg():
    assert hmdb2kegg('HMDB0003466') == ['C01040']
    
