import os

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        
        print("\n file found:\n")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")