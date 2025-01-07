import json 
from os.path import abspath, join

#f"/../../../static/json/{name_file}"
def read_json(name_file: str) -> dict:
    search_abs_path = abspath(join(__file__, "..", "..", "..", "static", "json", f"{name_file}"))
    with open(file= search_abs_path, mode= 'r') as file_json:
        return json.load(file_json)