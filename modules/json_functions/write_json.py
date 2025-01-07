import os, json
from os.path import abspath , join

#створюємо словарь для збереження нікнеймів та балів користувачів
list_users = {}


#створюємо словарь для збереження статусу сервера
list_server_status = {}

#__file__ + "/../../../static/json/utility.json")
#отримуємо дані з бази даних, яка знаходиться в папці static та у файлі data_base.json
with open(file = abspath(join(__file__, "..", "..", "..", "static", "json", "utility.json"))) as file:
    #загружаємо дані з json-файла в наш словник list_users
    list_server_status = json.load(file)
#__file__ + "/../../../static/json/data_base.json"
#отримуємо дані з бази даних, яка знаходиться в папці static та у файлі data_base.json
with open(file = abspath(join(__file__, "..", "..", "..", "static", "json", "data_base.json"))) as file:
    #загружаємо дані з json-файла в наш словник list_users
    list_users = json.load(file)

#os.path.abspath(__file__ + f"/../../../static/json/{filename}")
#функція для збереження даних  із словаря list_users у потрібний файл, у нашому випадку filename = "data_base.json"
def write_json(filename:str, object_dict: object) -> dict:
    #Формуємо абсолютний шлях до файлу, який знаходиться в папці static
    path_to_file = abspath(join(__file__, "..", "..", "..", "static", "json", f"{filename}"))
    #Відкриваємо файл у режимі запису ("w"), щоб зберегти в нього дані
    with open(path_to_file, "w") as file:
        json.dump(
            obj = object_dict,#Дані, які треба записати у нашому випадку, змінна словарь із користувачами list_users
            fp = file,#файл, куди будуть записані дані
            indent= 4, # Встановлюємо відступ у 4 пробіли для зручності читання у json файлі
            ensure_ascii= False#робимо так щоб окрім англ літер , могли записувати кирилицю
        )