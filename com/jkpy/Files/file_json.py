import json


def read_from_file(path):
    file = open(path)
    file_content_str = file.read()
    file.close()
    return file_content_str


def read_json_from_file(path):
    file = open(path)
    file_content_json = json.loads(file.read())
    file.close()
    return file_content_json

def read_json():
    file_content = read_from_file(path="/home/jayakumar/PycharmProjects/pyLearning/com/jkpy/Files/input_file.json")
    print(file_content)


read_json()