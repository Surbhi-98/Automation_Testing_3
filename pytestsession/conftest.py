import pytest
from api import app
import json

#----------------------------Fixture to test API--------------------------
@pytest.fixture
def run_api():
    print("Setup Code for run_api")
    response = app.test_client().get('/books')
    yield response
    print("Teardown Code for run_api")
@pytest.fixture
def run_api1(run_api):
    print("Setup Code for run_api1")
     #"Books_details" is json which i return from get_books.
    res = json.loads(run_api.data.decode('utf-8')).get("Books_details")
    yield  res
    print("Teardown Code for run_api1")

#------------------------------Autouse Fixtures(For conftest.py script inside of subdirectory action)---------------------------------
@pytest.fixture
def first_entry():
    print("Setup part of first_entry fixture of outer conftest.py file")
    yield "a", "b"
    print("\nTeardown part of first_entry fixture of outer conftest.py file")

@pytest.fixture
def order(first_entry):
    print("Setup part of order fixture of outer conftest.py file")
    yield []
    print("\nTeardown part of order fixture of outer conftest.py file")

@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    print("Setup part of append_first fixture of outer conftest.py file")
    yield order.append(first_entry)
    print("\nTeardown part of append_first fixture of outer conftest.py file")


#------------------------------class & Fixtures(For conftest.py script inside of subdirectory action)---------------------------------
class Addition:
    def sumition(a, b):
        c =a + b
        return c
    def substraction(a, b):
        c =a - b
        return c
    def multiplication(a, b):
        c =a * b
        return c

    def division(a, b):
        c =a / b
        return c

@pytest.fixture
def sum_number():
    print("Setup part of inner conftest.py file")
    yield Addition
    print("Teardown part of inner conftest.py file")

#-----------------------------------API Testing-----------------------------------------
# DATABASE
# Columns: | Player Id | Player Name | Team Name | Age | Average Score |
database = {
    1:["Akash", "A", 23, 58],
    2:["Archana", "B", 22, 60],
    3:["Vivek", "C", 23, 56],
    4:["Suman", "A", 24, 53]
}

# Input Payload
'''
    payload={
            "Player_id": id
        }
'''
class API:
    def get(test_payload):
        #id = payload["Player_id"]
        id = test_payload 
        if id in database:
            data=database[id]
            return {"Code":200, 
                "Response":{"Name":data[0],"Team":data[1],"Age":data[2],"Average":data[3]},
                "Message":"Read Operation Succesful"}
        else:
            return {"Code":404,"Message":"Player does not exists"}

@pytest.fixture
def get_player():
    print("Taking Input")
    yield API
    print("\nTeardown")

#------------------------------------------Fixture with module, session and function (bydefault) scope---------------------------------
class Addition:
    def sumition(a, b):
        c =a + b
        return c
    def substraction(a, b):
        c =a - b
        return c
    def multiplication(a, b):
        c =a * b
        return c

    def division(a, b):
        c =a / b
        return c
    
    def modulo(a, b):
        c = a % b
        return c 

@pytest.fixture(scope="module")
def sum_number():
    print("Taking Input for Fixture having scope module")
    yield Addition
    print("\nTeardown for Fixture having scope module")

@pytest.fixture
def sum_number1():
    print("Taking Input for Fixture with Bydefault scope")
    yield Addition
    print("\nTeardown for Fixture with Bydefault scope")

@pytest.fixture(scope="session")
def modulo_number():
    print("Taking Input for Fixture with session scope")
    yield Addition
    print("\nTeardown for Fixture with session scope")

#---------------------------------------------For Parameterized Test Case-----------------------------
class Addition:
    def sumition(a, b):
        c =a + b
        return c
    def substraction(a, b):
        c =a - b
        return c
    def multiplication(a, b):
        c =a * b
        return c

    def division(a, b):
        c =a / b
        return c

@pytest.fixture
def sum_number():
    print("Taking Input")
    yield Addition
    print("Teardown")

#------------------------------Class & Fixture---------------------------------
class Addition:
    def sumition(a, b):
        c =a + b
        return c
    def substraction(a, b):
        c =a - b
        return c
    def multiplication(a, b):
        c =a * b
        return c

    def division(a, b):
        c =a / b
        return c

@pytest.fixture
def sum_number():
    print("Taking Input")
    yield Addition
    print("Teardown")

#------------------------------Parameterized Fixture---------------------------------
@pytest.fixture(params=[3, 5])
def sum_number2(request):
    yield request.param
    print("Teardown") 

@pytest.fixture(params=[3, 5])
def sum_number3(request):
    a = request.param
    b = 7
    c = a + b
    yield c
    print("Teardown") 

@pytest.fixture(params=[3, 5])
def sum_number4(request):
    a = request.param
    if request.param == 3:
        c = a + 7
    if request.param == 5:
        c = a + 5
    yield c
    print("Teardown") 

#---------------------------------Taking Input Inside a class method for fixture---------------------
class Addition:
    def add():
        a = 3
        b = 4
        c = a + b
        return c
    def input1():
        a = 3
        return a
    def input2():
        b = 4
        return b

@pytest.fixture
def sum_number():
    print("Taking Input")
    yield Addition.add()
    print("Teardown") 

@pytest.fixture
def input_first_number():
    print("Taking Input")
    yield Addition.input1()
    print("Teardown") 

@pytest.fixture
def input_second_number():
    print("Taking Input")
    yield Addition.input1()
    print("Teardown") 


#------------------------------------Direct Define Fixtures---------------------
@pytest.fixture
def sum_number():
    a = 3
    b = 2
    c = a + b
    print("Taking Input")
    yield c
    print("Teardown")

@pytest.fixture
def input_first_number():
    a = 3
    yield a

@pytest.fixture
def input_second_number():
    b = 7
    yield b
