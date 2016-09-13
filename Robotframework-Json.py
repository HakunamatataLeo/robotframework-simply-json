import json

def read_json_file(pathToJson):
    """Return json contents as string of the given json path"""

    with open(pathToJson, 'r') as fp:
        data = json.load(fp)
        return data

def get_json_key_value(pathToJson, key):
    """Return the value of a key of the given json path"""

    return read_json_file(pathToJson)[key]

def set_json_key_value(pathToJson, key, value):
    """Set the value of a key of the given json path"""

    data = read_json_file(pathToJson)
    data[key] = value
    with open(pathToJson, 'w') as outfile:
        json.dump(data, outfile)
