import pytest

#----------------------------------------Test Cases for autouse fixture--------------------------------------------
# we not call fix_call1 fixture from inner conftest.py
def test_string_only(order, first_entry):
  print (order)
  print (first_entry)
  assert order == [first_entry]

def test_string_and_int(order, first_entry):
  order.append(2)
  assert order == [first_entry, 6]