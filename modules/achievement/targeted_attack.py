# from ..screens import list_grid , list_object_map 
# from ..classes.class_ship import list_ships

# ship_len = [1]# номер рядка и клеточки в этом рядке где отрисовываются зачеркиванные клеточки
# miss_row_achiv = [0]
# miss_col_achiv = [0]

# check_target_attack = ["None"]
# # направление поворота корабля
# list_direction_achiv = [""]
# # список клеток которые уже проверялись
# check_number_cell_achiv = []
# # флаг убитого корабля
# check_kill_achiv = [False]
# # длина корабля
# def target_attack():
#     if check_target_attack[0] != "Enemy did the target_attack achiv":
#         for rowee in range(len(list_grid)):
#             for cellee in range(len(list_grid[rowee])):
#                 if list_grid[rowee][cellee] == 7:
#                     check_target_attack[0] = "None"
#                     print("Доходит")
#                     miss_row_achiv[0] = rowee
#                     miss_col_achiv[0] = cellee
#                     str_cel = str(cellee)

#                     check_kill_achiv[0] = False
#                     list_direction_achiv[0] = ""
#                     ship_len[0] = 1
                    
#                     num_cell = (rowee * 10) + int(str_cel[-1])

#                     x = list_object_map[num_cell].x
#                     y = list_object_map[num_cell].y

#                     for ship in list_ships:
#                         if ship.X_COR == x and ship.Y_COR == y:
#                             ship_len[0] = ship.LENGHT
#                             list_direction_achiv[0] = ship.ORIENTATION_SHIP
#                             break

#                     if num_cell not in check_number_cell_achiv:
#                         if ship_len[0] == 1 and check_kill_achiv[0] != True:
#                             print("Убили однопалубный корабль")
#                             check_kill_achiv[0] = True
#                             check_number_cell_achiv.append(num_cell)
#                             check_target_attack[0] = "Enemy did the target_attack achiv"
#                             return

#                         if check_kill_achiv[0] == True:
#                             print("Корабль уже убит, пропускаем проверку")
#                             return

#                         elif list_direction_achiv[0] == "horizontal" and check_kill_achiv[0] != True:
#                             for len_ship in range(1 , ship_len[0]):
#                                 if list_grid[rowee][cellee + len_ship] == 7:
#                                     pass
#                                 elif list_grid[rowee][cellee + len_ship]!= 7:
#                                     break
#                                 if len_ship == ship_len[0] - 1:
#                                     print("убили корабль" , ship_len[0])
#                                     check_kill_achiv[0] = True
#                                     check_number_cell_achiv.append(num_cell)
        
#                         elif list_direction_achiv[0] == "vertical" and check_kill_achiv[0] != True:
#                             for len_ship in range(1 , ship_len[0]):
#                                 if list_grid[rowee + len_ship][cellee] == 7:
#                                     pass
#                                 elif list_grid[rowee + len_ship][cellee]!= 7:
#                                     break
#                                 if len_ship == ship_len[0] - 1:
#                                     print("убили корабль" , ship_len[0])
#                                     check_kill_achiv[0] = True
#                                     check_number_cell_achiv.append(num_cell)
                    
#                     if list_direction_achiv[0] == "vertical" and check_kill_achiv[0] == True:
#                         for anim_miss in range(0, ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] - 1 + anim_miss
#                             cellka = miss_col_achiv[0] - 1 
#                             if rowka == -1 or cellka == -1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False

#                         for anim_miss in range(0, ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] - 1 + anim_miss
#                             cellka = miss_col_achiv[0] 
#                             if rowka == -1 or cellka == -1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 7:
#                                         continue
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False
                                    
#                         for anim_miss in range(0, ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] - 1 + anim_miss
#                             cellka = miss_col_achiv[0] + 1 
#                             if rowka == -1 or cellka == -1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False                         
#                         if check_target_attack[0] == "None":
#                             check_target_attack[0] = "Enemy did the target_attack achiv"   
                            
#                     if list_direction_achiv[0] == "horizontal" and check_kill_achiv[0] == True:
#                         for anim_miss in range(0, ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] - 1
#                             cellka = miss_col_achiv[0] - 1 + anim_miss
#                             if rowka == -1 or cellka == -1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False

#                         for anim_miss in range(0 , ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] 
#                             cellka = miss_col_achiv[0] - 1 + anim_miss
#                             if rowka == -1 or cellka == - 1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 7:
#                                         continue
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False
                                    
#                         for anim_miss in range(0 , ship_len[0] + 2):
#                             rowka = miss_row_achiv[0] + 1
#                             cellka = miss_col_achiv[0] - 1 + anim_miss
#                             if rowka == -1 or cellka == - 1:
#                                 continue
#                             else:
#                                 if rowka <= 9 and cellka <= 9:
#                                     if list_grid[rowka][cellka] == 5:
#                                         check_target_attack[0] = False

#                         if check_target_attack[0] == "None":
#                             check_target_attack[0] = "Enemy did the target_attack achiv"
                    
                            
                                        
                                
                                

                
 