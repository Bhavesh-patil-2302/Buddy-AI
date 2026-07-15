from buddy.assistants import greet, tell_time, open_chrome, open_application , greet_new_user
from buddy.commands import APPS
from buddy.scanner.file_scanner import list_files
from buddy.memory.user_memory import save_user_data , load_user_data


APP_NAME = "Buddy AI"
VERSION = "v1.1.1"

print("=" * 40)
print(APP_NAME, VERSION)
print("=" * 40)

data=load_user_data()

if data is not None:
    name = data.get("name")
    age = data.get("age")
    greet(name)
else:
    print("Welcome to Buddy AI! Let's get to know you.")
    name = input("What's your name? ")
    age = int(input(f"How old are you, {name}? "))
    save_user_data(name, age)
    greet_new_user(name)
    

# greet(name)


# print(f"Wow, {age} years old! That's great to hear.")



# main menu
print()
print("What would you like to do today?")
print("1. say hello")
print("2. tell time")
print("3. open Google Chrome")
print("4. Show Current Version")
print("5. Open Applications")
print("6. Show available apps")
print("7. Scan files in a folder")

# user input for menu selection
choice = input("Please enter the number of your choice: ")

# handle user choice
if choice == "1":
    greet(name)

elif choice == "2":
    tell_time()

elif choice == "3":
    open_chrome()

elif choice == "4":
    print(f"Current version: {VERSION}")

elif choice == "5":
    app_name = input("Please enter the name of the application you want to open: ")
    open_application(app_name)

elif choice == "6":
    print("Available apps:")
    for app in APPS:
        print(f" - {app}")
elif choice == "7":
    path = input("Enter folder path: ")
    list_files(path)

else:
    print("Invalid choice. Please select a valid option from the menu.")
