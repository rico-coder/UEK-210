import os

file_path = os.path.join(os.path.dirname(__file__), "data.txt")

with open(file_path, "r") as f:
    contents = f.read()

print(contents)