from buddy.assistants import greet, tell_time, open_chrome, open_application , greet_new_user ,show_banner, show_banner_without_version
from buddy.commands import APPS
from buddy.scanner.file_scanner import list_files
from buddy.memory.user_memory import save_user_data , load_user_data
from buddy.memory.settings_manager import change_setting, load_settings

#preferences loading
settings = load_settings()

if settings.get("show_version"):
    show_banner()
else:
    show_banner_without_version()


#user data loading
data=load_user_data()


if data is not None:
    name = data.get("name")
    age = data.get("age")
    greet(name)
else:
    print("Welcome to Buddy AI! Let's get to know you.")
    name = input("What's your name? ")
    age = int(input(f"How old are you, {name}? "))
    print(f"Wow, {age} years old! That's great to hear.")
    save_user_data(name, age)
    greet_new_user(name)
    
if settings.get("show_time", True):
    tell_time()
else:
    print("Hope you are having a good time !")


# main menu
print()
print("What would you like to do today?")
print("1. say hello")
print("2. tell time")
print("3. open Google Chrome")
print("4. Open Applications")
print("5. Show available apps")
print("6. Scan files in a folder")
print("7. Modify Settings")

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
    app_name = input("Please enter the name of the application you want to open: ")
    open_application(app_name)

elif choice == "5":
    print("Available apps:")
    for app in APPS:
        print(f" - {app}")
elif choice == "6":
    path = input("Enter folder path: ")
    list_files(path)

elif choice == "7":
    print("Modify Settings:")
    result=change_setting("show_version",True)
    print(f"Change setting result: {result}")

else:
    print("Invalid choice. Please select a valid option from the menu.")

print(settings["show_time"])