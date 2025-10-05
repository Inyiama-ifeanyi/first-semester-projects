# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 18:46:23 2025

@author: ifeanyi
"""
# List of dictionaries 
students = []

def add_student():
    try: 
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        
        if not name.strip():
            return {'status': 'Error', 'message': 'Name cannot be empty'}
        if not isinstance(age, int) or age <= 0:
            return {'status': 'Error', 'message': 'Age must be positive integer'}
        if not 0 <= grade <= 100:
            return {'status': 'Error', 'message': 'Grade is not valid'}
        
        student = {"name": name, "age": age, "grade": grade}
        students.append(student)
        return {'status': 'Success', 'message': 'Student added successfully'}

    except ValueError:
        print('Error: Age and Grade must be numbers.')

def view_students():
    if not students:
        return {'status': 'Error', 'message': 'No student database found'}
    return students

def get_average_grade():
    if not students:
        return 0.0
    return sum([student['grade'] for student in students]) / len(students)
