import pytest

#---------------------Test cases------------------------

@pytest.mark.sum
def test_sum1():
    a = 3
    assert a + 1 == 7, "Test Failed"

def test_sum():
    a = 3
    b = 7
    assert a + b == 10, "Test Failed"

def test_sum2():
    a = 3
    b = 7
    assert a + 2 == b, "Test Failed"

@pytest.mark.sum
def test_sum3():
    a = 3
    b = 2
    c = a + b
    assert c == 5, "Test Failed"