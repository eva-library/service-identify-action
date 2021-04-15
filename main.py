import json
import requests
import logging.config
import sys
import os
import sqlite3
from flask import Flask, request, jsonify
from itertools import cycle
app = Flask(__name__)

class DataBase:    
    def __init__(self):
        print("BBDD")

    def identifyAction(self):

        try:
         # We save in a variable the request that comes from eva
            req_body = request.json
            action = ( req_body['openContext']['REQUEST_VARIBALE'])

        # returns in the EVA service cell the option by which the flow will go
            result = {
                "openContext":req_body["openContext"],
                "visibleContext":req_body["visibleContext"],
                "hiddenContext":req_body["hiddenContext"],
                "option" : action
            }
            # returns in JSON format the response in eva format
            return result

        except:
        # If any error happens, this is the answer with the formatvo eva
           result = {
                "openContext" : {},
                "visibleContext" : {},
                "hiddenContext": {},
                "option" : "ERROR"
            }
        # returns in JSON format the response in eva format
        return result


@app.route("/identify-action", methods=["POST"])

def test_functions(self):
    database = DataBase()    
    return database.identifyAction()
    
if __name__ == "__main__":
    app.run(debug=True, port=8003, ssl_context='adhoc')