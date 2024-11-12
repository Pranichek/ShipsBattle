import os, json

list_users = {}

with open(file = os.path.abspath(__file__ + "/../../../static/data_base.json")) as file:
    list_users = json.load(file)

def dump_json(filename):
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    with open(path_to_file, "w") as file:
        #dump - загрзука информации в джейсон файл
        json.dump(
            list_users,#значение которое записываем
            file,
            indent= 4,#сколько отступов будет в джейсон файле
            ensure_ascii= False#чтобы джейсон мог читать и записовать кирилицу 
        )