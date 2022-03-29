import pytest

import evenorodd

@pytest.mark.parametrize("a,b",[(10,True),(2,True),(3,True),(6,True),(5,False),(7,False)])
def test_evenorodd(a,b):
    result = evenorodd.EvenorOdd(a)
    assert result == b
