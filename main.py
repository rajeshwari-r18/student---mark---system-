import json
import os

DATA_FILE = 'students.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_student(data):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (comma separated): ").split(',')))
    data[name] = marks
    print(f"{name} added successfully.")

def view_student(data):
    name = input("Enter student name to view: ")
    if name in data:
        marks = data[name]
        avg = sum(marks)/len(marks)
        print(f"Marks: {marks}\nAverage: {avg:.2f}")
    else:
        print("Student not found!")

def main():
    data = load_data()
    while True:
        print("\n1. Add Student\n2. View Student\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student(data)
            save_data(data)
        elif choice == '2':
            view_student(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
