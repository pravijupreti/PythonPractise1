import os
import time


def check_file(file_Name):
    if os.path.exists(file_Name):
        pass
    else:
        if file_Name == "notebook.txt":
            print("No default notebook was found, created one.")
        else:
            with open(file_Name, "w") as file:
                print(f"No notebook with that name detected, created one.")
                pass
def read_notebook(file_Name):
    with open(file_Name, "r") as file:
        notebook_content = file.read()
        print(notebook_content)

def add_note(file_Name):
    new_note = input("Write a new note: ")
    timestamp = time.strftime(":::%H:%M:%S %m/%d/%y")
    note_with_timestamp = new_note + ":::" +timestamp
    with open(file_Name, "a") as file:
        file.write(note_with_timestamp + "\n")

def empty_notebook(file_Name):
    with open(file_Name, "w") as file:
        pass
    print("Notes deleted.")

file_Name = "notebook.txt"
# Main program loop
while True:
    check_file(file_Name)
    print(f"Now using file {file_Name}")
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Change the notebook")
    print("(5) Quit")

    # Prompt the user to select an option
    selection = input("\nPlease select one: ")

    if selection == "1":
        read_notebook(file_Name)
    elif selection == "2":
        add_note(file_Name)
    elif selection == "3":
        empty_notebook(file_Name)
    elif selection == "4":
        file_Name = input("Give the name of the new file: ")
        check_file(file_Name)
    elif selection == "5":
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
