import pytest

#---------------------------------------Pytest Dependencies uses Class & Fixtures-------------------------------------
@pytest.mark.dependency()
def test_sum_depen(sum_number):
  a = 3
  b = 4
  assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"
@pytest.mark.dependency()
def test_sub_depen(sum_number):
  a = 8
  b = 8
  assert sum_number.substraction(a, b) == 6, "Test Failed for test_sub"
@pytest.mark.dependency(depends=["test_sum_depen"])
def test_multi_depen(sum_number):
  a = 8
  b = 2
  assert sum_number.multiplication(a, b) == 16, "Test Failed for test_multi"

@pytest.mark.dependency(depends=["test_sum_depen, test_sub_depen"])
def test_division_depen(sum_number):
  a = 8
  b = 2
  assert sum_number.division(a, b) == 6, "Test Failed for test_divi"

#---------------------------------------Uses Module, Bydefault Scope Fixtures-------------------------------------
# def test_sum(sum_number):
#     a = 3
#     b = 4
#     assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"

# def test_sub(sum_number):
#     a = 8
#     b = 8
#     assert sum_number.substraction(a, b) == 0, "Test Failed for test_sub"

# def test_multi(sum_number1):
#     a = 8
#     b = 2
#     assert sum_number1.multiplication(a, b) == 14, "Test Failed for test_multi"

# def test_divi(sum_number):
#     a = 8
#     b = 2
#     assert sum_number.division(a, b) == 4, "Test Failed for test_divi"

#--------------------------------Parameterized Test Case-----------------------------------------------
# @pytest.mark.parametrize("a, b", [(3, 4), (5, 2), (1, 42)])
# def test_sum(sum_number, a, b):
#     # a = 3
#     # b = 4
#     assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"

# def test_sub(sum_number):
#     a = 8
#     b = 8
#     assert sum_number.substraction(a, b) == 6, "Test Failed for test_sub"

# def test_multi(sum_number):
#     a = 8
#     b = 2
#     assert sum_number.multiplication(a, b) == 16, "Test Failed for test_multi"

# def test_divi(sum_number):
#     a = 8
#     b = 3
#     assert sum_number.division(a, b) == 16, "Test Failed for test_divi"
#--------------------------------Uses Class & Fixture---------------------------
# def test_sum(sum_number):
#     a = 3
#     b = 4
#     assert sum_number.sumition(a, b) == 7, "Test Failed for test_sum"

# def test_sub(sum_number):
#     a = 8
#     b = 8
#     assert sum_number.substraction(a, b) == 6, "Test Failed for test_sub"

# def test_multi(sum_number):
#     a = 8
#     b = 2
#     assert sum_number.multiplication(a, b) == 16, "Test Failed for test_multi"

# def test_divi(sum_number):
#     a = 8
#     b = 3
#     assert sum_number.division(a, b) == 16, "Test Failed for test_divi"



#---------------------------------Uses Parameterized Fixture---------------------------------
# def test_sum5(sum_number2):
#     assert sum_number + 1 == 4, "Test Failed for test_sum3"
#     assert sum_number + 1 == 6, "Test Failed for test_sum4"
#     # assert sum_number == 4, "Test Failed for test_sum3"
#     # print("Test Finished")

# # def test_sum6(sum_number2):
# #     assert sum_number + 1 == 6, "Test Failed for test_sum4"
# #     # assert sum_number == 6, "Test Failed for test_sum4"

# def test_sum7(sum_number3):
#     assert sum_number1 == 12, "Test Failed for test_sum3"
#     # print("Test Finished")

# def test_sum8(sum_number4):
#     assert sum_number1 == 10, "Test Failed for test_sum3"
#     # print("Test Finished")




#-------------------------------taking Fixtures whose input based on class--------------------  
# def test_sum3(sum_number):
#     assert sum_number == 7, "Test Failed for test_sum3"
#     # print("Test Finished")

# def test_sum4(sum_number):
#     assert sum_number == 5, "Test Failed for test_sum4"

# @pytest.mark.add
# def test_sum1(input_first_number):
#     assert input_first_number + 1 == 4, "Test Failed for test_sum1" 

# def test_sum(input_first_number, input_second_number):
#     assert input_first_number + input_second_number == 10, "Test Failed for test_sum"

# @pytest.mark.add
# def test_sum2(input_first_number, input_second_number):
#     assert input_first_number + 4 == input_second_number, "Test Failed for test_sum2"

#--------------------------Direct use fixture from conftest.py script-------------------------- 
# def test_sum3(sum_number):
#     assert sum_number == 5, "Test Failed for test_sum3"
#     # print("Test Finished")

# def test_sum4(sum_number):
#     assert sum_number == 10, "Test Failed for test_sum4"
#     # print("Test Finished")

# @pytest.mark.add
# def test_sum1(input_first_number):
#     assert input_first_number + 1 == 7, "Test Failed for test_sum1" 

# def test_sum(input_first_number, input_second_number):
#     assert input_first_number + input_second_number == 10, "Test Failed for test_sum"

# @pytest.mark.add
# def test_sum2(input_first_number, input_second_number):
#     assert input_first_number + 4 == input_second_number, "Test Failed for test_sum2"