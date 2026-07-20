# important imports 
from datetime import datetime
import webbrowser
import subprocess
from buddy.commands import APPS
from buddy.core.app_info import APP_NAME, VERSION
from buddy.core.settings_metadata import SETTINGS_METADATA
from buddy.memory.settings_manager import change_setting, load_settings
from buddy.memory.user_memory import save_user_data , load_user_data



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


# settings modifier
def settings_modifications():
    settings=load_settings()
    print("Modify Settings:")
    print(">"*5 ," SETTINGS MENU  " ,"<"*5  )
    print("which settings do you want to change ??")
    setting_keys = []
    for number , (key,details) in enumerate(SETTINGS_METADATA.items(),start=1):
        display_name=details.get("display_name")
        value=settings.get(key)
        status="ON" if value else "OFF"
        print(f"{number}. {display_name}: {status}")
        setting_keys.append(key)
    back_number=len(setting_keys)+1
    print(f"{back_number}. Back")
    user_preference=int(input("enter the number of the setting that you wanna change !!   "))
    if user_preference==back_number:
        print("going back")
        return
    else:
        selected_key=setting_keys[user_preference - 1]
        print(f"you selected {selected_key}")
        setting_type=SETTINGS_METADATA[selected_key].get("type")
        #for toggle settings
        if setting_type==bool:
            current_value = settings.get(selected_key)
            new_value = not current_value
            print(f"{selected_key} changed to {new_value}")
            status=change_setting(selected_key,new_value)
            print(status)
        else:#for dynamic settings
            pass #i'll add these later when i get a non toggleable setting
