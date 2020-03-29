import json

import requests


def parse_emp_get_respose():
    url = "http://dummy.restapiexample.com/api/v1/employees"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    print("status code is: ")
    print(response.status_code)
    json_output_dist = json.loads(response.text)

    print(json_output_dist)

    print("END OF FILE")

parse_emp_get_respose()
