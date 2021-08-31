import pytest
from bridgedbpy.get_organism_code import *

def test_get_organism_code():
    res = get_organism_code("Escherichia coli")
    assert res == "Ec"
