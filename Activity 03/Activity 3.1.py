#This asks the user to input their first name, last name, and age.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")


#This concatenates the first name and last name into a full name
full_name = first_name + " " + last_name


#This slices the first name
sliced_name = first_name[:3]  # Extracting the first three characters


#This creates a greeting message
greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old."


#This prints all the results
print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting_message)
