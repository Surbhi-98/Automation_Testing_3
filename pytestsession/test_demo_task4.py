import pytest

#---------------------------------Uses Parameterized Fixture---------------------------------
def test_sum5(sum_number2):
    assert sum_number + 1 == 4, "Test Failed for test_sum3"
    assert sum_number + 1 == 6, "Test Failed for test_sum4"
    # assert sum_number == 4, "Test Failed for test_sum3"
    # print("Test Finished")

# def test_sum6(sum_number2):
#     assert sum_number + 1 == 6, "Test Failed for test_sum4"
#     # assert sum_number == 6, "Test Failed for test_sum4"

def test_sum7(sum_number3):
    assert sum_number1 == 12, "Test Failed for test_sum3"
    # print("Test Finished")

def test_sum8(sum_number4):
    assert sum_number1 == 10, "Test Failed for test_sum3"
    # print("Test Finished")