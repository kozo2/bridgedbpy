import pytest
from bridgedbpy.get_system_code import *

def test_get_system_code():
    res = get_system_code("Ensembl")
    assert res == "En"
