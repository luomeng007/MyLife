# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/179:53
software: PyCharm

Description:
    read data from .csv file
"""
main_scene_name = []
main_scene_type = []
main_scene_directory = []
main_scene_left = []
main_scene_top = []

with open("./dataBase/mainInterface.csv", "r") as f:
    all_data = f.readlines()
    # print(all_data[0])
    for data_list in all_data[1:]:
        new_list = data_list.rstrip().split(",")
        main_scene_name.append(new_list[0])
        main_scene_type.append(new_list[1])
        main_scene_directory.append(new_list[2])
        main_scene_left.append(int(new_list[3]))
        main_scene_top.append(int(new_list[4]))


print(main_scene_name)
print(main_scene_type)
print(main_scene_directory)
print(main_scene_left)
print(main_scene_top)
print(type(main_scene_name))
print(type(main_scene_type))
print(type(main_scene_directory))
print(type(main_scene_left))
print(type(main_scene_top))
