import pygame , os , random 
from .shop_image import shop_item
from ..server import enemy_died_ships , player_died_ships

#класс для тексту в магазині
class Font_Shop:
    # конструктор (__init__) тексту в магазині
    def __init__(self, size: int, name_font: str, text: str, x_cor: int, y_cor: int, target_y: int , max_width: int, max_height: int , text_color: str):
        self.TEXT_COLOR = text_color
        self.SIZE = size
        self.NAME_FONT = name_font
        self.PATH_TO_FONT = os.path.abspath(__file__ + f"/../../../media/fonts/{self.NAME_FONT}")
        self.TEXT = text
        self.X_COR = x_cor
        self.Y_COR = y_cor
        self.TARGET_Y = target_y
        self.MAX_WIDTH = max_width
        self.MAX_HEIGHT = max_height
        self.SPEED = 10
        self.VISIBLE = 0
        self.TURN = "Down"
        self.ACTIVE = False
        # Создаем шрифт
        self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
        # Рендер текста
        text_surface = self.font.render(self.TEXT, False, self.TEXT_COLOR)
        # Масштабирование текста до заданных размеров
        self.text_surface = pygame.transform.scale(text_surface,(self.MAX_WIDTH, self.MAX_HEIGHT))
        self.text_surface = self.text_surface.convert_alpha()
     # Плавно змінює прозорість кнопки:fade_in() збільшує прозорість до 255 (повністю видимий стан)
    def fade_in(self):
        if self.VISIBLE < 255:
            self.VISIBLE += 5
            if self.VISIBLE >= 255:
                self.VISIBLE = 255

    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        if self.VISIBLE > 0:
            self.VISIBLE -= 5
            if self.VISIBLE <= 0:
                self.VISIBLE = 0

    # Зображення може плавно переміщатися вниз (до цільової позиції) і назад
    # Використовується прапорець turn, щоб визначити напрямок руху
    # Викликається fade_in() і fade_out() для плавного з’явлення чи зникнення
    def move(self):
        if self.ACTIVE:
            if self.TURN == "Down":
                if self.Y_COR < self.TARGET_Y:
                    self.Y_COR += self.SPEED
                    self.fade_in()
                    if self.Y_COR >= self.TARGET_Y:
                        self.Y_COR = self.TARGET_Y
                        self.TURN = "Up"

            elif self.TURN == "Up":
                if self.Y_COR > -(self.SIZE + (832 - (self.TARGET_Y + self.SIZE))):
                    self.Y_COR -= self.SPEED
                    self.fade_out()
                    if self.Y_COR <= -(self.SIZE + (832 - (self.TARGET_Y + self.SIZE))):
                        self.Y_COR = -(self.SIZE + (832 - (self.TARGET_Y + self.SIZE)))
                        self.TURN = "Down"

        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.SIZE + (832 - (self.TARGET_Y + self.SIZE))):
            self.ACTIVE = False

    def update_text(self):
        if int(self.TEXT) == 0:
            self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
            self.text_surface = self.font.render(self.TEXT, False , self.TEXT_COLOR)
        elif int(self.TEXT) >= 100:
            self.MAX_WIDTH = 100
            self.MAX_HEIGHT = 105
            self.X_COR = 455
            self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
            self.text_surface = self.font.render(self.TEXT, False , self.TEXT_COLOR)
            self.text_surface = pygame.transform.scale(self.text_surface,(self.MAX_WIDTH, self.MAX_HEIGHT))
        elif int(self.TEXT) > 0 and int(self.TEXT) < 100:
            self.MAX_WIDTH = 100
            self.MAX_HEIGHT = 105
            self.X_COR = 457
            self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
            self.text_surface = self.font.render(self.TEXT, False , self.TEXT_COLOR)
            self.text_surface = pygame.transform.scale(self.text_surface,(self.MAX_WIDTH, self.MAX_HEIGHT))

     # відмальовка тексту із заданою прозорістю
    def draw(self, screen: pygame.Surface):
        self.text_surface.set_alpha(self.VISIBLE)
        screen.blit(self.text_surface, (self.X_COR, self.Y_COR))

# створюємо списки із завданнями , щоб кожен раз вони були рандомні
list_first_task = [
    "2 hits in a row" , 
    "4 hits in a row" ,
    "Kill one three-decker ship", 
    "3 hits in a row",
    ]
list_second_task = [
    "Buy one bonus from the store" , 
    "Survive 5 turns without losing a ship" , 
    "Kill two ships in a row" , 
    "The first to kill a 3 deck ship" 
    ]
list_third_task = [
    "The first to kill a 4 deck ship", 
    "Kill 4 single-deck ships in a row", 
    "Kill 3 double-decker ships in a row", #
    "kill two three-decker ships in a row" 
    ]
list_fourth_task = [
    "The first step is murder" , 
    "Kill three ships in a row" , 
    "Completed the first three tasks" ,#
    "8 hits in a row"
    ]


# лист збереження грошей
money_list = [0]

#1
two_hits_in_a_row = []
def two_hits_in_row(number_cell: int):
    if "True" not in two_hits_in_a_row:
        count_ships = 0
        two_hits_in_a_row.append(number_cell)

        for cell in two_hits_in_a_row:
            if cell != 5 and cell != 0:
                count_ships += 1
            else:
                two_hits_in_a_row.clear()
                return False
            
        if count_ships > 1 and "True" not in two_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Two hits in a row")
            two_hits_in_a_row.append("True")

# 1 three hits in a row
three_hits_in_a_row = []
def three_hits_in_row(cell: int):
    if "True" not in three_hits_in_a_row:
        count_ships = 0
        three_hits_in_a_row.append(cell)

        for cell in three_hits_in_a_row:
            if cell!= 5 and cell != 0:
                count_ships += 1
            else:
                three_hits_in_a_row.clear()
                return False
        if count_ships > 2 and "True" not in three_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Three hits in a row")
            three_hits_in_a_row.append("True")


#1
four_hits_in_a_row = []
def four_hits_in_row(number_cell: int):
    if "True" not in four_hits_in_a_row:
        count_ships = 0
        four_hits_in_a_row.append(number_cell)

        for cell in four_hits_in_a_row:
            if cell!= 5 and cell != 0:
                count_ships += 1
            else:
                four_hits_in_a_row.clear()
                return False
        if count_ships > 3 and "True" not in four_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Four hits in a row")
            four_hits_in_a_row.append("True")

#4 8 hits in a row
egight_hits_in_a_row = []
def eight_hits_in_row(number_cell: int):
    count_ships = 0
    egight_hits_in_a_row.append(number_cell)

    for cell in egight_hits_in_a_row:
        if cell!= 5 and cell != 0:
            count_ships += 1
        else:
            egight_hits_in_a_row.clear()
            return False
    if count_ships > 7 and "True" not in egight_hits_in_a_row:
        check_completed_tasks[0] += 1
        print("Eight hits in a row")
        egight_hits_in_a_row.append("True")


# 1  убить один трехапалубный корабль
kill_three_deckcer_ship = [0]
def kill_one_three_decker_ship():
    if kill_three_deckcer_ship[0] != "kill three deck ship":
        if enemy_died_ships[0] != "yes":
            if 3 in enemy_died_ships[0]:
                kill_three_deckcer_ship[0] += 1

            if kill_three_deckcer_ship[0] >= 1:
                kill_three_deckcer_ship[0] = "kill three deck ship"
                check_completed_tasks[0] += 1
                print("Ты убил один трехбалубный кораблик")


# kill two ships in a row
ship_hits = []
kill_count = [0]
count_zero = [0]
def kill_two_ships_in_a_row():
    if enemy_died_ships[0] != "yes":
        if kill_count[0] != "Kill two ships":
            kill_count[0] = len(enemy_died_ships[0]) - count_zero[0] 

            if 0 in ship_hits or 5 in ship_hits:
                count_zero[0] += 1
                ship_hits.clear()
                kill_count[0] = 0
                return False

            if kill_count[0] >= 2:
                kill_count[0] = "Kill two ships"
                check_completed_tasks[0] += 1
                print("Ты убил два корабля подряд")

#3 Kill 3 double-decker ships in a row
count_two_3decker_ship = []
check_killed_for_double_ships = []
start_index_two = [0]
def kill_three_double_decker_in_a_row():
    # count_two_3decker_ship.append(cell)
    two = count_two_3decker_ship.count(2)
    check_killed_for_double_ships.clear()
    check_killed_for_double_ships.extend(enemy_died_ships[0][start_index_two[0]:])
    if two > 0:
        if two <= 1:
            check_killed_for_double_ships.clear()

        if two <= 1:
            if 0 in count_two_3decker_ship:
                for i in range(0 , len(count_two_3decker_ship)):
                    if count_two_3decker_ship[i] == 0:
                        del count_two_3decker_ship[i]

        if "You kill two three decker in row" not in count_two_3decker_ship:
            if count_two_3decker_ship.count(0) > 0 and two > 1:
                    count_two_3decker_ship.clear()
                    two = 0
                    return False
            
            if count_two_3decker_ship.count(1) >= 1 and two > 1 and 1 in check_killed_for_double_ships:
                count_two_3decker_ship.clear()
                two = 0
                return False
            
            if count_two_3decker_ship.count(3) >= 3 and two > 1 and 3 in check_killed_for_double_ships:
                count_two_3decker_ship.clear()
                two = 0
                return False
            
            if count_two_3decker_ship.count(4) >= 4 and two > 1 and 4 in check_killed_for_double_ships:
                count_two_3decker_ship.clear()
                two = 0
                return False
            
            if two == 6 and "You kill two three decker in row" not in count_two_3decker_ship:
                count_two_3decker_ship.append("You kill two three decker in row")
                check_completed_tasks[0] += 1
                print("Ты убил три двухпалубных кораблей подряд")
    else:
        count_two_3decker_ship.clear()
        if enemy_died_ships[0] != "yes" and len(enemy_died_ships[0]) >= start_index_two[0]:
            start_index_two[0] += 1

# kill four single ships in a row
single_ships = []
check_killed_for_single_ships = []
start_index_single = [0]
def kill_four_single_ships_in_a_row():
    one = single_ships.count(1)
    check_killed_for_single_ships.clear()
    check_killed_for_single_ships.extend(enemy_died_ships[0][start_index_single[0]:])
    if one > 0:
        if one <= 0:
            check_killed_for_single_ships.clear()

        if one <= 0:
            if 0 in single_ships:
                for i in range(0 , len(single_ships)):
                    if single_ships[i] == 0:
                        del single_ships[i]

        if single_ships.count(0) > 0 and one > 0:
            single_ships.clear()
            one = 0
            return False
            
        if single_ships.count(2) >= 2 and one > 0 and 2 in check_killed_for_single_ships:
            single_ships.clear()
            one = 0
            return False
        
        if single_ships.count(3) >= 3 and one > 0 and 3 in check_killed_for_single_ships:
            single_ships.clear()
            one = 0
            return False
        
        if single_ships.count(4) >= 4 and one > 0 and 4 in check_killed_for_single_ships:
            single_ships.clear()
            one = 0
            return False

        if one == 4 and "Kill four single ships in a row" not in single_ships:
            single_ships.append("Kill four single ships in a row")
            check_completed_tasks[0] += 1
            print("You are kill four single ships in a row")
    else:
        single_ships.clear()
        if enemy_died_ships[0] != "yes" and len(enemy_died_ships[0]) >= start_index_single[0]: 
            start_index_single[0] += 1


#3 kill two three-decker ships in a row
count_three_ships = []
check_killed_for_three_ships = []
start_index = [0]
def kill_two_three_decker_in_a_row():
    count_three = count_three_ships.count(3)
    check_killed_for_three_ships.clear()
    check_killed_for_three_ships.extend(enemy_died_ships[0][start_index[0]:])
    if count_three > 0:
        if count_three <= 2:
            check_killed_for_three_ships.clear()

        if count_three <= 2:
            if 0 in count_three_ships:
                for i in range(0 , len(count_three_ships)):
                    if count_three_ships[i] == 0:
                        del count_three_ships[i]

        if count_three_ships.count(0) > 0 and count_three >= 3:
                print(count_three , count_three_ships.count(0))
                count_three_ships.clear()
                count_three = 0
                print("с ноликом")
                return False
        if count_three_ships.count(1) >= 1 and count_three >= 3 and 1 in check_killed_for_three_ships:
            count_three_ships.clear()
            count_three = 0
            print("с еденичкой")
            return False
            
        if count_three_ships.count(2) >= 2 and count_three >= 3 and 2 in check_killed_for_three_ships:
            count_three_ships.clear()
            count_three = 0
            print("с двоейчкой")
            return False
        if count_three_ships.count(4) >= 4 and count_three >= 3 and 4 in check_killed_for_three_ships: 
            count_three_ships.clear()
            count_three = 0
            print("с четверочкой")
            return False
        print(count_three , "count_tree")
        print(check_killed_for_three_ships)
        if count_three == 6 and "Kill two three decker in a row" not in count_three_ships:
            check_completed_tasks[0] += 1
            count_three_ships.append("Kill two three decker in a row")
            print("Ты убил два трехпалубных кораблей подряд")

    else:
        count_three_ships.clear()
        if enemy_died_ships[0]!= "yes" and len(enemy_died_ships[0]) >= start_index[0]:
            start_index[0] += 1


#3 первым убить четыреx палубный корабль
our_ships_4decker = [0]
enemy_ships_4decker = [0]
def first_kill_four_decker():
    if enemy_ships_4decker[0] != "kill four-decker ship":
        if type(enemy_died_ships[0]) != str:
            our_ships_4decker[0] = 0
            enemy_ships_4decker[0] = 0
            print(type(enemy_died_ships[0]))
            our_ships_4decker[0] = 1 - player_died_ships.count(4)
            enemy_ships_4decker[0] = 1 - enemy_died_ships[0].count(4)

            if enemy_ships_4decker[0] != "kill four-decker ship":
                if our_ships_4decker[0] > enemy_ships_4decker[0] and enemy_ships_4decker[0] == 0 and enemy_ships_4decker[0]!= "kill four-decker ship":
                    enemy_ships_4decker[0] = "kill four-decker ship"
                    check_completed_tasks[0] += 1
                    print("Ты первым убил четырехпалубный корабль")

#2 The first to kill a 2 deck ship
our_ships_3decker = [0]
enemy_ships_3decker = [0]
def first_kill_three_decker():
     if type(enemy_died_ships[0]) != str:
        our_ships_3decker[0] = 0
        if enemy_ships_3decker[0] != "kill three-decker ship":
            enemy_ships_3decker[0] = 0

        our_ships_3decker[0] = 2 - player_died_ships.count(3)
        enemy_ships_3decker[0] = 2 - enemy_died_ships[0].count(3)
        if enemy_ships_3decker[0] != "kill three-decker ship":
            if our_ships_3decker[0] >= enemy_ships_3decker[0] and enemy_ships_3decker[0] == 1 and enemy_ships_3decker[0] != "kill three-decker ship":
                enemy_ships_3decker[0] = "kill three-decker ship"
                check_completed_tasks[0] += 1
            



# первый удар убийство
count_shot = [0]
def first_shot_is_kill(cell):
    count_shot[0] += 1
    if cell == 1 and count_shot[0] == 1:
        count_shot.append("You are kill ship in one shot")
        check_completed_tasks[0] += 1
        print("You are first shot is kill")


#2  выжить 5 раз чтобы твои корабли не подбили ниразу
count_turns = [0]
save_sevens = []
def kept_all_ships_alive_for_five_turns(grid: object):
    count_turns[0] += 1
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 7 and (row * 10) + cell not in save_sevens:
                count_turns[0] = 0
                save_sevens.append((row * 10) + cell)

    if count_turns[0] >= 6 and "True" not in count_turns:
        print("У тебя целы корабли 5 раундов")
        check_completed_tasks[0] += 1
        count_turns.append("True")



# kill three ships in a row
ship_hits_three = []
count_zero_thrible = [0]
count_kill_three = [0]
def kill_three_ships_in_a_row():
    if enemy_died_ships[0] != "yes":
        if count_kill_three[0] != "You killes three ships in row":
            count_kill_three[0] = len(enemy_died_ships[0]) - count_zero_thrible[0]

            if 0 in ship_hits_three or 5 in ship_hits_three:
                count_zero_thrible[0] += 1
                ship_hits_three.clear()
                count_kill_three[0] = 0
                return False
             
            if count_kill_three[0] >= 3:
                count_kill_three[0] = "You killes three ships in row"
                check_completed_tasks[0] += 1
                print("Ты убил три корабля подряд")



check_completed_tasks = [0]
def complete_three_tasks():
    if check_completed_tasks[0] != 999:
        if check_completed_tasks[0] == 3:
            check_completed_tasks[0] = 999
            print("Ты выполнил все три завдання")


# створюємо текст із рандомним першим завданням
first_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(45 + (832 - (136 + 45))),
    size = 45 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_first_task),
    target_y = 136 , 
    max_width = 161 ,
    max_height = 31 ,
    text_color = "White"
)

# створюємо текст iз рандомним другим завданням
second_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(25 + (832 - (192 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_second_task),
    target_y = 192 , 
    max_width = 220 ,
    max_height = 28 ,
    text_color = "White"
)

# створюємо текст iз рандомним третьим завданням
third_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(25 + (832 - (244 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = list_third_task[0],
    target_y = 244 ,
    max_width = 180 ,
    max_height = 28 , 
    text_color = "White"
)

# створюємо текст iз рандомним четвертим завданням
fourth_task = Font_Shop(
    x_cor = 52 ,
    y_cor = - (25 + (832 - (298 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_fourth_task),
    target_y = 298 ,
    max_width = 225 ,
    max_height = 31 , 
    text_color = "White"
)

player_balance = Font_Shop(
    x_cor = 475 ,
    y_cor = - (96 + (832 - (190 + 96))),
    size = 96 ,
    name_font = "Jersey15.ttf",
    text = str(money_list[0]),
    target_y = 190 ,
    max_width = 62 ,
    max_height = 105 , 
    text_color = "Yellow"
)



# додаємо тексти до списку shop_item для відображення їх за допомогою циклу
shop_item.extend([first_task , second_task , third_task , fourth_task , player_balance])

    