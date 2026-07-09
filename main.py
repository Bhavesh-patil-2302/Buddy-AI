from buddy.assistants import greet, tell_time, open_chrome, open_application
from buddy.commands import APPS


APP_NAME = "Buddy AI"
VERSION = "v0.9.0"

print("=" * 40)
print(APP_NAME, VERSION)
print("=" * 40)




name = input("What's your name? ")

greet(name)

age = input(f"How old are you, {name}? ")
print(f"Wow, {age} years old! That's great to hear.")

# main menu
print()
print("What would you like to do today?")
print("1. say hello")
print("2. tell time")
print("3. open Google Chrome")
print("4. Show Current Version")
print("5. Open Applications")
print("6. Show available apps")

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
else:
    print("Invalid choice!")