import os, json

#створюємо словарь для збереження нікнеймів та балів користувачів
list_users = {}


#отримуємо дані з бази даних, яка знаходиться в папці static та у файлі data_base.json
with open(file = os.path.abspath(__file__ + "/../../../static/data_base.json")) as file:
    #загружаємо дані з json-файла в наш словник list_users
    list_users = json.load(file)


#функція для збереження даних  із словаря list_users у потрібний файл, у нашому випадку filename = "data_base.json"
def dump_json(filename):
    #Формуємо абсолютний шлях до файлу, який знаходиться в папці static
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    #Відкриваємо файл у режимі запису ("w"), щоб зберегти в нього дані
    with open(path_to_file, "w") as file:
        json.dump(
            list_users,#Дані, які треба записати у нашому випадку, змінна словарь із користувачами list_users
            file,#файл, куди будуть записані дані
            indent= 4, # Встановлюємо відступ у 4 пробіли для зручності читання у json файлі
            ensure_ascii= False#робимо так щоб окрім англ літер , могли записувати кирилицю
        )