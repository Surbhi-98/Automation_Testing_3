import pytest

#-------------------------------taking Fixtures whose input based on class--------------------  
def test_sum3(sum_number):
    assert sum_number == 7, "Test Failed for test_sum3"
    # print("Test Finished")

def test_sum4(sum_number):
    assert sum_number == 5, "Test Failed for test_sum4"

@pytest.mark.add
def test_sum1(input_first_number):
    assert input_first_number + 1 == 4, "Test Failed for test_sum1" 

def test_sum(input_first_number, input_second_number):
    assert input_first_number + input_second_number == 10, "Test Failed for test_sum"

@pytest.mark.add
def test_sum2(input_first_number, input_second_number):
    assert input_first_number + 4 == input_second_number, "Test Failed for test_sum2"