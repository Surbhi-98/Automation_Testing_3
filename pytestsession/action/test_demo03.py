import pytest

#----------------------------------------------Test Cases for Nested conftest.py (Fixture sum_number from root conftest file)----------------------------
def test_sum1(fix_call):
    a = 3
    b = 4
    assert fix_call.sumition(a, b) == 17, "Test Failed for test_sum"

def test_sub1(fix_call):
    a = 8
    b = 8
    assert fix_call.substraction(a, b) == 0, "Test Failed for test_sub"
