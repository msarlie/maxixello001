import json
import os

DATA_FILE = "students.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def register_student(data):
    print("\n--- Register New Student ---")
    student_id = input("Enter Student ID: ").strip()
    if student_id in data:
        print("❌ Error: ID already exists!")
        return
    name = input("Enter Full Name: ").strip()
    course = input("Enter Course: ").strip()
    if not student_id or not name or not course:
        print("❌ Error: Blanks not allowed!")
        return
    data[student_id] = {"name": name, "course": course}
    save_data(data)
    print(f"✅ Success: {name} registered!")

def view_students(data):
    print("\n--- Student List ---")
    if not data:
        print("No records found.")
        return
    print(f"{'ID':<12} | {'Name':<25} | {'Course':<25}")
    print("-" * 68)
    for student_id, info in data.items():
        print(f"{student_id:<12} | {info['name']:<25} | {info['course']:<25}")

def search_student(data):
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to find: ").strip()
    if student_id in data:
        info = data[student_id]
        print(f"📌 Found! ID: {student_id}\nName: {info['name']}\nCourse: {info['course']}")
    else:
        print("❌ Student ID not found.")

def edit_student(data):
    print("\n--- Edit Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()
    if student_id in data:
        print(f"Current Info -> Name: {data[student_id]['name']} | Course: {data[student_id]['course']}")
        new_name = input("Enter New Name (or press Enter to keep current): ").strip()
        new_course = input("Enter New Course (or press Enter to keep current): ").strip()
        
        if new_name:
            data[student_id]['name'] = new_name
        if new_course:
            data[student_id]['course'] = new_course
            
        save_data(data)
        print("✏️ Success: Student profile updated!")
    else:
        print("❌ Student ID not found.")

def delete_student(data):
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id in data:
        name = data[student_id]['name']
        del data[student_id]
        save_data(data)
        print(f"🗑️ Success: {name}'s record has been removed.")
    else:
        print("❌ Student ID not found.")

def main():
    student_database = load_data()
    while True:
        print("\n=== STUDENT REGISTRATION SYSTEM ===")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Edit Student Profile")
        print("5. Delete Student Record")
        print("6. Exit")
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            register_student(student_database)
        elif choice == "2":
            view_students(student_database)
        elif choice == "3":
            search_student(student_database)
        elif choice == "4":
            edit_student(student_database)
        elif choice == "5":
            delete_student(student_database)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()