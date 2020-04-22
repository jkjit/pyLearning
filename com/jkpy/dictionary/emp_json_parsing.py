import requests
import json

from com.jkpy.Files.file_json import read_from_file

"""
{
    "status": "success",
    "data": [
                {
                    "id": "1",
                    "employee_name": "Tiger Nixon",
                    "employee_salary": "320800",
                    "employee_age": "61",
                    "profile_image": ""
                },
                {
                    "id": "2",
                    "employee_name": "Garrett Winters",
                    "employee_salary": "170750",
                    "employee_age": "63",
                    "profile_image": ""
                }
            ]
}
"""


# getting user details like Phone and email
def get_byname(input_emp_name):
    url = "http://dummy.restapiexample.com/api/v1/employees"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    json_output_dist = json.loads(response.text)

    json_output_dist['data']

    data_list = json_output_dist['data']
    details_found = False
    for details in data_list:
        if details['employee_name'] == input_emp_name:
            details_found = True
            print("Employee by name {} found. ".format(input_emp_name))
            print(" {} age is : {}".format(input_emp_name, details['employee_age']))

    if not details_found:
        print("Employee entered as {} not found".format(input_emp_name))


def parse_emp_from_file():
    file_content = read_from_file(path="/home/jayakumar/PycharmProjects/pyLearning/com/jkpy/Files/input_file.json")
    json_output_dist = json.loads(file_content)
    # print(json_output_dist)
    try:
        data_list = json_output_dist['data']
        print("data list {}".format(data_list))

        for emp_obj in data_list:
            print("Emp Id: {}, Emp Name: {}".format(emp_obj['id'], emp_obj['employee_name']))
    except:
        print("Error in getting the data ;;;;;sfa;fas;f")

def parse_emp_get_respose():
    url = "http://dummy.restapiexample.com/api/v1/employees"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    # response = requests.head(url)

    print("Lets printout #################################")
    print(response)
    print("End of response #################################")

    print(response.text)
    json_output_dist = json.loads(response.text)
    # print(json_output_dist)
    try:
        data_list = json_output_dist['data']
        print("data list {}".format(data_list))

        for emp_obj in data_list:
            print("Emp Id: {}, Emp Name: {}".format(emp_obj['id'], emp_obj['employee_name']))
    except:
        print("Error in getting the data ;;;;;sfa;fas;f")

def try_outs():
    get_byname("Tiger Nixon")

    get_byname("Garrett Winters")

    get_byname("JK")

    get_byname("Doris Wilder")

    parse_emp_get_respose()

def lookup_employee_from_user_input():
    print("Hello welcome!")
    proceed = True
    while proceed:
        input_emp_name = input("Enter a employee name to get age : ")
        if input_emp_name == '':
            proceed = False
        else:
            get_byname(input_emp_name)


# lookup_employee_from_user_input()
# parse_emp_get_respose()

# parse_emp_get_respose()
# parse_emp_from_file()
parse_emp_get_respose()