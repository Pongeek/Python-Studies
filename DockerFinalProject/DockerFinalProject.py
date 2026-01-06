import sys
from flask import Flask
import json
import os
import logging
import printColors

logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler(sys.stdout)
    ]
)
app = Flask(__name__)

try:
    with open("config.json") as config:
        allowed_names_list = json.load(config)
        allowed_names = set(allowed_names_list)
        print("Allowed names:")
        for allowed_name in allowed_names_list:
            print(allowed_name)
except FileNotFoundError:
    logging.critical("Error accessing config file")

@app.route("/")
def welcome():
    print("The user has accessed the path")
    return printColors.printBlack("Welcome to my system, Please login")

@app.route("/login/<login>")
def newPath(login):
    logging.info("The user has accessed the login with the name " + login)
    if login in allowed_names:
        logging.info("Name " + login + " exists in the config file" )
        response = printColors.printGreen("Access granted")
    else:
        logging.warning("Name " + login + " does not exist in the config file")
        response = printColors.printRed("Access denied")
    return response

@app.route("/addName/<login>")
def addName(login):
    if login in allowed_names_list:
        response = printColors.printRed("Name " + login + " already exists in the config file")
    else:
        allowed_names_list.append(login)
        with open("config.json", "w") as config:
            json.dump(allowed_names_list, config, indent=4)
        response = printColors.printGreen("Added " + login + " to the config file successfully")
    return response



if __name__ == "__main__":
    app.run(host=os.environ.get("HOST_IP"), port=80, debug=True) # We can


