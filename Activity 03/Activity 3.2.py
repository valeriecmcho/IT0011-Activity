#This asks the user to input their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

#This concatenates the first name and last name into a full name
full_name = first_name + " " + last_name

# Convert full name to upper and lower case
upper_case_name = full_name.upper()
lower_case_name = full_name.lower()

#This calculates the length of the full name including whitespaces
name_length = len(full_name)

#This prints all the results
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", upper_case_name)
print("Full Name (Lower Case):", lower_case_name)
print("Length of Full Name:", name_length)
