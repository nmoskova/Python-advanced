import os

while True:
    command = input()
    if command == "End":
        break

    data = command.split("-")
    action, file_name = data[0], data[1]
    if action == "Create":
        created_file = open(file_name, "w")
        created_file.close()

    elif action == "Add":
        content = data[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        old_string, new_string = data[2], data[3]
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            with open(file_name, "r+") as file:
                file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(file_content)

    elif action == "Delete":
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            os.remove(file_name)