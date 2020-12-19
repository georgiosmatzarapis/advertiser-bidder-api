# Python libs.
import pytest
import requests
import json
import os.path
# Project files.
from fixtures.conf_test import supply_url as URL


input1_path = "test_data/test-case-1-input.json"
input2_path = "test_data/test_case_2_input.json"
output1_path = "test_data/test_case_1_expected_output.json"

# Load test files.
if (os.path.isfile(input1_path) and 
    os.path.isfile(input2_path) and
    os.path.isfile(output1_path)):

    with open(input1_path) as file:
        input1 = json.load(file)
    with open(input2_path) as file:
        input2 = json.load(file)
    with open(output1_path) as file:
        output1 = json.load(file)
else:
    exit(1)

def test_case_1(URL):
	url = URL
	resp = requests.post(url, json=input1)
	assert resp.status_code == 200
	assert resp.json() == output1

def test_case_2(URL):
	url = URL
	resp = requests.post(url, json=input2)
	assert resp.status_code == 204
	assert resp.text == ""