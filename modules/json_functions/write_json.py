import os , json

list_users = {}

with open(file = os.path.abspath(__file__ + f"/../../../static/data_base.json")) as file:
    list_users = json.load(file)


def write_json(filename:str):
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    with open(path_to_file, 'w') as file:
        json.dump(list_users,
                file,
                indent= 4,
                ensure_ascii= False
                )
    