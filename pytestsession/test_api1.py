import pytest
from flask import json
from api import app
# To execute the below test cases we run the python -m pytest -v -s pytestsession\test_api1.py command in terminal  

def test_books(run_api, run_api1):
    assert run_api.status_code == 200, "Test Failed"
    assert type(run_api1[0]) is dict, "Test Failed"
    assert type(run_api1[1]) is dict, "Test Failed"
    assert run_api1[0]['author'] == 'Havard', "Test Failed"
    assert run_api1[1]['author'] == 'Will', "Test Failed"
    assert type(run_api1) is list, "Test Failed"

def test_books1(run_api1):
    assert run_api1[0]['id'] == 1, "Test Failed"
    assert run_api1[1]['title'] == 'Will', "Test Failed"

# def test_books():
#     response = app.test_client().get('/books')
#     #"Books" is json which i return from get_books.
#     res = json.loads(response.data.decode('utf-8')).get("Books_details")
#     assert response.status_code == 200, "Test Failed"
#     assert type(res[0]) is dict, "Test Failed"
#     assert type(res[1]) is dict, "Test Failed"
#     assert res[0]['author'] == 'Havard', "Test Failed"
#     assert res[1]['author'] == 'Will', "Test Failed"
#     assert type(res) is list, "Test Failed"
