import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"
# def sum_it(x,y):
#     return x + y
# def test_equal():
#     assert sum_it(5, 3) == 10

def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200

def test_get_booking_by_id():
   response = requests.get(f'{base_url}/1')
   response_data = response.json()
   expected_keys = [
       "lastname",
       "totalprice",
       "depositpaid",
       "bookingdates",
       "additionalneeds"
   ]
   assert response.status_code == 200
