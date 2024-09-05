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