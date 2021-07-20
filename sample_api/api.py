from flask import json, request, jsonify
from os import listdir
from os.path import isfile, join
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

files = [f for f in listdir("sample_api/resources") if isfile(join("sample_api/resources", f))]

def download(file_identifier):
    if file_identifier:
        logger.info("Received " + file_identifier)
        if file_identifier in files:
            with open(f"sample_api/resources/{file_identifier}", 'r') as f:
                lines = f.read()
            with open (f"sample_api/downloads/{file_identifier}", 'w') as f:
                f.write(lines)
                return jsonify(message = "Downlading file " + file_identifier)
        else:
            return(jsonify(message = "File not found"))
    logger.warning("file_identifier is not provided")


# Create a handler for our search (GET) applications
def search(appName=None, os=None, version=None, limit=None):
    logger.info("Received query " + str(request.query_string.decode("utf-8")))
    param_list = []
    if appName:
        param_list.append(appName)
    if os:
        param_list.append(os)
    if version:
        param_list.append(str(version))
    # print("Searching for application")
    search_result = [x for x in files if all(y in x for y in param_list)]
    if limit:
        param_list.append(limit)
    
    result = sorted(sorted(sorted(search_result, key= lambda app: app.split("-")[2]), key=lambda app: app.split("-")[1]),key=lambda app: app.split("-")[0])
    logger.info("Found applications " + str(result))
    return jsonify(application = result[:limit]) if limit in param_list else jsonify(application = result)