import pytest

#-----------------------------Uses Fixture with module, session scope--------------------
def test_modulo(modulo_number):
    a = 10
    b = 3
    assert modulo_number.modulo(a, b) == 3, "Test Failed for test_modulo"

def test_divi(sum_number):
    a = 8
    b = 2
    assert sum_number.division(a, b) == 4, "Test Failed for test_divi"
