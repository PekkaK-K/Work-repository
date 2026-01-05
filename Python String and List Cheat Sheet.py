Python String and List Cheat Sheet
String Interpolation 
name = "Jill"

interpolation = f"Hello, {name}"

# result > 'Hello, Jill'

greeting_format = "Hello, {}. How are you?"

formatted = greet_format.format(name)

# result > 'Hello, Jill. How are you?'
String Utilities
"hello,world".upper()

# result > 'HELLO, WORLD'

"HELLO, WORLD".lower()

# result > 'HELLO, WORLD'

"Hello, Jill".replace("Hello", "Hey")

# result > 'Hey, Jill'
List Slices
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

NAMES[0]
# result > 'John'

NAMES[1]
# result > 'Paul'

NAMES[:2]
# result > ['John', 'Paul']

NAMES[2:]
# result > ['George', 'Ringo']

NAMES[::-1]
# result > ['Ringo', 'George', 'Paul', 'John']

NAMES[::2]
# result > ['John', 'George']
List Utilities
sum(AGES)
# result > 86

min(AGES)
# result > 20

max(AGES)
# result > 23
Iteration Utilities
# Looping through each name in NAMES
for name in NAMES:
    print(name)
# result > 'John', 'Paul', 'George', 'Ringo'

# Looping through each name and age using zip
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")
# result > 'John 20', 'Paul 21', 'George 22', 'Ringo 23'

# Looping through NAMES in reverse order
for name in reversed(NAMES):
    print(name)
# result > 'Ringo', 'George', 'Paul', 'John'

# Using range to print numbers 0 through 4
for i in range(5):
    print(i)
# result > 0, 1, 2, 3, 4

# Using enumerate to get index and name from NAMES
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
# result > '0 John', '1 Paul', '2 George', '3 Ringo'

Working with CSV and JSON
Import Libraries
import csv       # For reading/writing CSV files

import json      # For handling JSON data

from pprint import pprint  # For pretty-printing dictionaries
Create a Dictionary and Convert to JSON
EINSTEIN = {

    "birthplace": "Germany",

    "name": "Albert",

    "surname": "Einstein",

    "born": "1879-03-14",

    "category": "Physics",

    "motivation": "For his services to Theoretical Physics..."
}

# Convert dictionary to JSON string

einstein_json = json.dumps(EINSTEIN)

print(einstein_json)

# result > JSON string with Einstein's data
Convert JSON String Back to Dictionary
back_to_dict = json.loads(einstein_json)

pprint(back_to_dict)

# result > Original dictionary format, pretty-printed
Read CSV File and Store Data in a List of Dictionaries
with open("laureates.csv", "r") as f:

    reader = csv.DictReader(f)

    laureates = list(reader)

# result > List of dictionaries, each representing a row from "laureates.csv"
 

Filter Data Based on Condition (Names Starting with "A")
laureates_beginning_with_a = []

for laureate in laureates:

    if laureate['name'][0] == "A":

        laureates_beginning_with_a.append(laureate)

# result > List of laureates with names that start with "A"
 

Write Filtered Data to a JSON File
with open("laureates.json", "w") as f:

    json.dump(laureates_beginning_with_a, f, indent=2)

# result > JSON file "laureates.json" with data of laureates starting with "A"

Python Web Development Resources
 

Django Documentation Tutorial
Flask Documentation Tutorial
Creating APIs with Django Rest Framework
Building APIs with FastAPI