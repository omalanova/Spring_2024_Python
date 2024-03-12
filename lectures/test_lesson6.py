# import pytest
# import requests
#
# base_url = "https://restful-booker.herokuapp.com/booking"
# auth_url = "https://restful-booker.herokuapp.com/auth"
# # def sum_it(x,y):
# #     return x + y
# # def test_equal():
# #     assert sum_it(5, 3) == 10
#
# def test_get_code():
#     result = requests.get(base_url)
#     print(result)
#     assert result.status_code == 200
#
# def test_get_booking_by_id():
#    response = requests.get(f'{base_url}/1')
#    response_data = response.json()
#    # print(response_data)
#    expected_keys = [
#        # "firstname",
#        "lastname",
#        "totalprice",
#        "depositpaid",
#        "bookingdates",
#        "additionalneeds",
#        # "country"
#    ]
#    assert response.status_code == 200
#    assert len(expected_keys) == len(response_data.keys())
#    for key in expected_keys:
#        assert key in response_data.keys()
#
# def test_create_booking():
#     response = requests.post(base_url)
#     payload = {
#         "firstname" : "James",
#         "lastname" : "Brown",
#         "totalprice" : 150,
#         "depositpaid" : True,
#         "bookingdates" : {
#         "checkin" : "2024-01-01",
#         "checkout" : "2024-01-01"
#         },
#         "additionalneeds" : "Breakfast"
#     }
#     response = requests.post(base_url, json=payload)
#     print(response.json()['bookingid'])
#     assert response.status_code == 200
# def test_check_created_booking():
#     result = requests.get(f'{base_url}/211') #надо обновлять тест test_create_booking(), чтобы получить актуальный id (211 не постоянный id)
#     print(result.json())
#     assert result.status_code == 200
#     assert result.json()['firstname'] == "James"
#
# def test_get_token():
#     authdata = {
#         "username" : "admin",
#         "password" : "password123"
#     }
#     response = requests.post(auth_url, json=authdata)
#     token = response.json()["token"]
#     print(token)
#     assert response.status_code == 200
#
# def test_update_booking():
#     payload = {
#         "firstname" : "James",
#         "lastname" : "Brown",
#         "totalprice" : 150,
#         "depositpaid" : False,
#         "bookingdates" : {
#         "checkin" : "2024-01-01",
#         "checkout" : "2024-01-01"
#         },
#         "additionalneeds" : "Lunch"
#     }
#     token = {"Cookie": "token=d671d26c55b5689"} #надо обновлять токен в тесте test_get_token() и сразу же запускать
#
#     response = requests.put(f'{base_url}/1041', json=payload, headers=token) #надо обновлять тест test_create_booking(), чтобы получить актуальный id (1041 не постоянный id)
#     assert response.status_code == 200
#     response_2 = requests.get(f'{base_url}/1041')
#     assert response_2.json()['additionalneeds'] == "Lunch"
