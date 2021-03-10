#Author: Max Lawrie
#Date: 2021-03-10

#This test script verifies the acceptance criteria specified for the assignment. 

import requests
import json

#The URL of the API to be tested
url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
   
#Make a GET request and store the response
response = requests.get(url)
   
#Validate status code
assert response.status_code == 200

#Store the JSON contents
response_body = response.json()

#Acceptance Criteria #1: Name = "Carbon credits"
def test_Name():
    assert response_body['Name'] == 'Carbon credits'

#Acceptance Criteria #2: CanRelist = true
def test_CanRelist():
    assert response_body['CanRelist'] == True

#Acceptance Criteria #3: The Promotions element with Name = "Gallery" has a Description
#that contains the text "2x larger image"
def test_Gallery():
    promotions = response_body['Promotions']
    for promotion in promotions:
        if promotion['Name'] == 'Gallery':
            assert promotion['Description'] == '2x larger image'