import pytest

#--------------------------------Uses Class & Fixture---------------------------
def test_sum(sum_number):
    a = 3
    b = 4
    assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"

def test_sub(sum_number):
    a = 8
    b = 8
    assert sum_number.substraction(a, b) == 6, "Test Failed for test_sub"

def test_multi(sum_number):
    a = 8
    b = 2
    assert sum_number.multiplication(a, b) == 16, "Test Failed for test_multi"

def test_divi(sum_number):
    a = 8
    b = 3
    assert sum_number.divis