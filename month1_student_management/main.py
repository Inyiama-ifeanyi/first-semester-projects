# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 20:18:35 2025

@author: ifeanyi
"""
from pprint import pprint
from student_data import add_student, view_students, get_average_grade
while True:
    print("1. Add Student\n2. View Students\n3. Get Average Grade\n4. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        result = add_student()
        print(result)
    if choice == "2":
        result = view_students()
        pprint(result)
    if choice == "3":
        result = get_average_grade()
        print(result)
    if choice == "4":
        print('Exiting Program')
        break
    else:
        print('Invalid choice: Select 1 - 4')
        