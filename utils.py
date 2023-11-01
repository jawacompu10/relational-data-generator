import json


def read_json_file(file_path: str):
    with open(file_path) as schema_file:
        return json.load(schema_file)
