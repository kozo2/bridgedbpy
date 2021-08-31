import pytest
from bridgedbpy.get_full_name import *

def test_get_full_name():
    res = get_full_name('Ce')
    assert res == "ChEBI"
