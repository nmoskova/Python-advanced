import os
from os import path

file_extensions = {}
extension = ""

for file in os.listdir():
    if path.isdir(file):
        continue

    elif path.isfile(file):
        extension = "." + file.split(".")[1]
        if extension not in file_extensions:
            file_extensions[extension] = []

    file_extensions[extension].append(file)

desktop = os.path.expanduser('~') + '\Desktop'
file_name = "report.txt"
file_path = os.path.join(desktop, file_name)

with open(file_path, "w") as report_file:
    for ext, files in sorted(file_extensions.items()):
        report_file.write(f"{ext}\n")
        for file in sorted(files):
            report_file.write(f"---{file}\n")