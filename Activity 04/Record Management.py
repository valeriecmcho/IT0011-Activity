import json
import os

class StudentRecordManager:
    def __init__(self):
        self.records = []
        self.filename = None

    def load_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.records = json.load(file)
            self.filename = filename
            print("File loaded successfully.")
        else:
            print("File not found.")

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.records, file)
            print("File saved successfully.")
        else:
            print("No file selected. Use 'Save As' option.")

    def save_as_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.records, file)
        self.filename = filename
        print("File saved as", filename)

    def show_all_records(self):
        for record in self.records:
            print(record)

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x[1][1])
        print("Records ordered by last name.")

    def order_by_grade(self):
        self.records.sort(key=lambda x: x[2] * 0.6 + x[3] * 0.4, reverse=True)
        print("Records ordered by grade.")

    def show_student_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Student not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    def edit_record(self, student_id, class_standing=None, major_exam=None):
        for index, record in enumerate(self.records):
            if record[0] == student_id:
                new_record = (
                    record[0],
                    record[1],
                    class_standing if class_standing is not None else record[2],
                    major_exam if major_exam is not None else record[3]
                )
                self.records[index] = new_record
                print("Record updated successfully.")
                return
        print("Student not found.")

    def delete_record(self, student_id):
        self.records = [record for record in self.records if record[0] != student_id]
        print("Record deleted successfully.")


def main():
    manager = StudentRecordManager()
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            filename = input("Enter filename: ")
            manager.load_file(filename)
        elif choice == '2':
            manager.save_file()
        elif choice == '3':
            filename = input("Enter filename: ")
            manager.save_as_file(filename)
        elif choice == '4':
            manager.show_all_records()
        elif choice == '5':
            manager.order_by_last_name()
        elif choice == '6':
            manager.order_by_grade()
        elif choice == '7':
            student_id = input("Enter student ID: ")
            manager.show_student_record(student_id)
        elif choice == '8':
            student_id = input("Enter student ID (6 digits): ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing: "))
            major_exam = float(input("Enter major exam grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == '9':
            student_id = input("Enter student ID to edit: ")
            class_standing = input("Enter new class standing (leave blank to keep unchanged): ")
            major_exam = input("Enter new major exam grade (leave blank to keep unchanged): ")
            manager.edit_record(
                student_id,
                float(class_standing) if class_standing else None,
                float(major_exam) if major_exam else None
            )
        elif choice == '10':
            student_id = input("Enter student ID to delete: ")
            manager.delete_record(student_id)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
