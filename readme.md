
# UMBA's Financial service api

This is the umba python senior software engineer test to create a python based REST server with the following resources and endpoints (account, transactions and users) using Flask
and postgres. Each endpoint has the required object and database model where
required, correct validation of inputs, unit tests that test against the REST endpoints and with mocked third party dependencies where required.

Each endpoint is properly documented on openapi, <a href="localhost:5000/docs.">see localhost:5000/docs.</a>


## Installation
for pythonistas like me

```bash
  - Setup your virtual environment
  - Install required dependecies
  - You can run the project from main.py or run the file from terminal
    
    sh start.sh
```

for docker dudes

```bash
  - run the below from terminal, that should take care of the rest
  
  docker build -t azeez010/umba-test
  docker-compose up
```

## Running Tests
To run tests, run the following command

```bash
   pytest
```


## Tech Stack

**Programming Languages:** Python

**Frame Work:** Python FLASK

**Container Tech:** Docker and Docker Compose


To check the documentation run, visit localhost:5000/docs

## Support

For support or questions, email dataslid@gmail.com