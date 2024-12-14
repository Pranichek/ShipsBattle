import json 
import os

def read_json(name_file: str):
    search_abs_path = os.path.abspath(__file__ + f"/../../../static/json/{name_file}")
    with open(file= search_abs_path, mode= 'r') as file_json:
        return json.load(file_json)