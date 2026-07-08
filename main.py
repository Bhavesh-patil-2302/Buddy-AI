APP_NAME = "Buddy AI"
VERSION = "v0.5.0"

print("=" * 40)
print(APP_NAME, VERSION)
print("=" * 40)

name = input("What's your name? ")

print()
print(f"Hello, {name}! 👋")
print("Welcome to Buddy AI.")

age = input(f"How old are you, {name}? ")
print(f"Wow, {age} years old! That's great to hear.")

# main menu
print()
print("What would you like to do today?")
print("1. say hello")
print("2. tell time")
print("3. Exit")
print("4. Show Current Version")

# user input for menu selection
choice = input("Please enter the number of your choice: ")

# handle user choice
if choice == "1":
    print(f"Hello {name}! 👋")

elif choice == "2":
    print("Current time feature coming soon...")

elif choice == "3":
    print("Goodbye!")

elif choice == "4":
    print(f"Current version: {VERSION}")

else:
    print("Invalid choice!")

