# important imports 
from datetime import datetime
import webbrowser
import subprocess
from buddy.commands import APPS
from buddy.core.app_info import APP_NAME, VERSION

#tell time function
def tell_time():
    current_time = datetime.now()
    print(f"\n 🕒 Current Time: {current_time.strftime('%I:%M:%S %p')}")

#opening banner if  user wants version to be shown
def show_banner():
    print("=" * 40)
    print(APP_NAME, VERSION)
    print("=" * 40)

#opening banner if user does not want version to be shown
def show_banner_without_version():
    print("=" * 40)
    print(APP_NAME)
    print("=" * 40)

#opening browser function
def open_chrome():
    webbrowser.open("https://www.google.com")
    print("Opening Google Chrome...")


#greet  function if user is not new
def greet(name):
    print(f"Welcome Back, {name}! 👋")
    print("What should I help You Today ?")

#greet function if user is new
def greet_new_user(name):
    print(f"Welcome to Buddy AI, {name}! 👋")
    print("What's Up !! I am Buddy AI, your personal assistant. I can help you with various tasks and make your life easier. Let's get started!")


#Opening application
def open_application(app_name):
    app_name = app_name.lower()
    command = APPS.get(app_name)

    if command:
        subprocess.Popen(command)
        print(f"Opening {app_name}...")
    else:
        print(f"Sorry, I don't know how to open '{app_name}'.")