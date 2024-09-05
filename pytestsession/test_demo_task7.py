import pytest

#---------------------------------------Uses Module, Bydefault (function) Scope Fixtures-------------------------------------
def test_sum(sum_number):
    a = 3
    b = 4
    assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"

def test_sub(sum_number):
    a = 8
    b = 8
    assert sum_number.substraction(a, b) == 0, "Test Failed for test_sub"

def test_multi(sum_number1):
    a = 8
    b = 2
    assert sum_number1.multiplication(a, b) == 14, "Test Failed for test_multi"

def test_divi(sum_number):
    a = 8
    b = 2
    assert sum_number.division(a, b) == 4, "Test Failed for test_divi"