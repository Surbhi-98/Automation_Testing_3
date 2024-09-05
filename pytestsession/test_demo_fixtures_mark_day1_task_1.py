import pytest

#------------------------------------Test cases using fixtures-----------------------

@pytest.fixture
def sum_number():
    a = 3
    b = 2
    c = a + b
    return c

@pytest.fixture
def input_first_number():
    a = 3
    return a

@pytest.fixture
def input_second_number():
    b = 7
    return b

@pytest.mark.add
def test_sum1(input_first_number):
    assert input_first_number + 1 == 7, "Test Failed" 

def test_sum(input_first_number, input_second_number):
    assert input_first_number + input_second_number == 10, "Test Failed"
@pytest.mark.add
def test_sum2(input_first_number, input_second_number):
    assert input_first_number + 4 == input_second_number, "Test Failed" 

def test_sum3(sum_number):
    assert sum_number == 5, "Test Failed"
