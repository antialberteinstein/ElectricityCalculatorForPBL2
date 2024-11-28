import json
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Enter the path of the JSON file: ")
try:
    with open(path, 'r') as file:
        data = json.load(file)
        for key, value in data.items():
            print(f"{key}: {value}")
except FileNotFoundError:
    print("File not found.")
