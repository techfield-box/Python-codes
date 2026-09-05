# 5.1 Student Record System (Dictionaries, CSV files)

import csv

students = {}

def student_system():
    while True:
        print("\n--- XII Student Records ---")
        print("1. Add/Update\n2. Search\n3. Display All\n4. Export to CSV\n5. Exit")
        choice = input("Select (1-5): ")

        if choice == '1':
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            students[roll] = {'Name': name, 'Marks': marks}
            print("Record saved!")

        elif choice == '2': 
            roll = input("Enter Roll Number to search: ")
            if roll in students:
                print(f"Found: {students[roll]}")
            else:
                print("Student not found.")

        elif choice == '3':
            for roll, info in students.items():
                print(f"Roll: {roll} | Name: {info['Name']} | Marks: {info['Marks']}")

        elif choice == '4':
            with open('students.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Roll No', 'Name', 'Marks'])
                for roll, info in students.items():
                    writer.writerow([roll, info['Name'], info['Marks']])
            print("Data exported to students.csv")

        elif choice == '5':
            break


student_system()