APP_NAME = "Buddy AI"
VERSION = "v0.3.0"

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

# user input for menu selection
choice = input("Please enter the number of your choice: ")