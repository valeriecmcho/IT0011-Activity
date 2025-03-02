# This asks the user to input their first name, Last name, Age, Contact No#, and Course
last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")


# This formats the user input
student_info = (
    f"Last Name: {last_name}\n"
    f"First Name: {first_name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact_number}\n"
    f"Course: {course}\n"
    "-------------------------\n"
)

# This opens the file for appending and writes the information to the txt file
with open("students.txt", "a") as file:
    file.write(student_info)

# This displays the confirmation message
print("\nStudent information has been saved to 'students.txt'.")
