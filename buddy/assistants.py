# important imports 
from datetime import datetime
import webbrowser
import subprocess
from buddy.commands import APPS

#tell time function
def tell_time():
    current_time = datetime.now()
    print(f"\n 🕒 Current Time: {current_time.strftime('%I:%M:%S %p')}")


#opening browser function
def open_chrome():
    webbrowser.open("https://www.google.com")
    print("Opening Google Chrome...")


#greet  function
def greet(name):
    print(f"Hello, {name}! 👋")
    print("Welcome to Buddy AI.")


#Opening application
def open_application(app_name):
    app_name = app_name.lower()
    command = APPS.get(app_name)

    if command:
        subprocess.Popen(command)
        print(f"Opening {app_name}...")
    else:
        print(f"Sorry, I don't know how to open '{app_name}'.")