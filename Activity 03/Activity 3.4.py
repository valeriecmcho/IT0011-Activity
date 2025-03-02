# This opens the file in read mode
with open("students.txt", "r") as file:
        # This reads the contents of the file
        student_data = file.read()
   
    # This displays the student information
print("\nReading Student Information:\n")
print(student_data)