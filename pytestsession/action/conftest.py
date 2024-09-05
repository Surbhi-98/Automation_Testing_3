import pytest

#----------------------------------------Call a Fixture sum_number from root conftest file(test\pytestsession\conftest.py)---------------------------------
@pytest.fixture
def fix_call(sum_number):
    print("Setup part of outer conftest.py file")
    yield sum_number 
    print("Teardown part of outer conftest.py file")

#----------------------------------------Autouse Fixtures(For conftest.py script inside of subdirectory action)-------------
#Below Fixture is autouse Fixture
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    print("Setup part of append_first fixture of inner conftest.py file")
    yield order.append(first_entry)
    print("\nTeardown part of append_first fixture of inner conftest.py file")

# @pytest.fixture(autouse=True)
# def fix_call1(append_first):
#     print("Setup part of  inner conftest.py file")
#     yield append_first 
#     print("\nTeardown part of inner conftest.py file")