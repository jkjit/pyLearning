import json


def read_from_file(path):
    file = open(path)
    file_content_str = file.read()
    file.close()
    return file_content_str


def test_read_file(path):
    with open(path, 'r') as f:
        return f.read()


def test_json_read(path):
    result = test_read_file(path)
    json_content = json.loads(result)
    return json_content


def read_json_from_file(path):
    file = open(path)
    file_content_json = json.loads(file.read())
    file.close()
    return file_content_json


def read_json():
    file_content = read_from_file(path="/home/jayakumar/PycharmProjects/pyLearning/com/jkpy/Files/input_file.json")
    print(file_content)

content = test_read_file("/home/jayakumar/PycharmProjects/pyLearning/com/jkpy/Files/input_file.json")
print(content)
print(read_json_from_file("/home/jayakumar/PycharmProjects/pyLearning/com/jkpy/Files/input_file.json"))
# read_json()
