import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20]

import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    display_width = year["value"] // 10_000_000
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)

    import csv
from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return "your code here!"


@app.route("/laureates/")
def laureate():
    return "your code here!"


app.run(debug=True)

import csv
from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    return jsonify(laureates)


app.run(debug=True)

from flask import Flask

app = Flask(__name__)

from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)

import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    # Your code here!
    return "your code here!"


app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


app.run(debug=True)

import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    search_string = request.args.get("surname").lower().strip()

    for laureate in laureates:
        if search_string in laureate["surname"].lower():
            results.append(laureate)

    return jsonify(results)


app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


app.run(debug=True)

import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()

    # tip: remember that laureate["name"] contains a first name
    for laureate in laureates:
        surname = laureate["surname"].lower()
        # your code here
        if search_string in surname:
            results.append(laureate)

    return jsonify(results)


app.run(debug=True)

mport csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()

    # tip: remember that laureate["name"] contains a first name
    for laureate in laureates:
        surname = laureate["surname"].lower()
        first_name = laureate['name'].lower()
        # your code here
        if (search_string in surname) or (search_string in first_name):
            results.append(laureate)

    return jsonify(results)


app.run(debug=True)

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who speaks in rhyme.",
        },
        {
            "role": "user",
            "content": "Who was Alexander Hamilton?",
        }
    ],
    model=model_name,
    temperature=1.0,
    max_tokens=1000,
    top_p=1.0
)

print(response.choices[0].message.content)