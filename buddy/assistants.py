# important imports 
from datetime import datetime
import webbrowser

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