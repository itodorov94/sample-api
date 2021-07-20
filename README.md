# Via Download Service Solution

This repository contains a simple API for finding and downloading applications. 

## Tools/Libraries  


### Python

Used version 3.7

### Pip 

Used verion 19.2.3
### OpenAPI
Openapi or the Openapi Specification (OAS), defines a standard language agnostic approach to
developing RESTful APIs, which are both human and machine readable. 


### Connexion
Connexion is a Python library that "automagically" handles HTTP requests based on your OAS. It acts as a
simple wrapper around Flask reducing the boilerplate code you have to write as well. So we still
have access to all the functionality we would have when developing a normal Flask web API. 


## API

Now onto actually developing our API.

### Project Structure

The API has the following structure and is defined using OAS(OpenAPI Specifications)

```text
sample-api/
├── downloads/
├── resources/
├── swagger/
|   ├── app.yaml
|   └── mock_token.yaml
├── test/
|    ├── __init__.py
|    └── __test_api.py
├── __main__.py
├── api.py
└── mock_token_server.py
```

The file `__main__.py` starts the `connexion` application and in `api.py` are defined the two functions to handle the endpoints `/search` and `/download`. `mock_token_server.py` starts the mock server used for the authentication. In the folder `resources` are the sample text file which simulate an application and in `downloads` will be the files downloaded. In folder `test` are the tests written for the two endpoints. Folder `swagger` containts the 2 files for the OAS for the API and for the mocked authentication server. 

### Start the API Server

#### Install the required dependencies
Execute `pip install -r requirements.txt` 

#### Start the server and the mocked auth server
Execute `python sample_api/mock_token_server.py &` and `python sample_api/__main__.py` 

### Test the API

To test the API  run `python sample_api/test/test_api.py` . This will run all tests written.


### Example request

#### Search


Execute `curl --header 'Authorization: Bearer 123'  http://localhost:5000/api/search` 


#### Download

Execute `curl --header 'Authorization: Bearer 123'  http://localhost:5000/api/download?file_identifier=[file_identifier]` 

More detailed documentacion can be found on the Swagger UI generated page on `http://localhost:5000/api/ui`



