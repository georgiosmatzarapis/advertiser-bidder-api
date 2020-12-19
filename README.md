# Avertiser Bidder API

The main goal of this project is to visualize the API functionalities using the Flask-RESTPlus library. Also, a mock advertiser bidder has been developed.

## Installation

### Run project
  - Install [pipenv](https://pipenv.readthedocs.io/en/latest/)
    ```
    pip install pipenv
    ```
  - Change to src directory and install depedencies
    ```
    cd src
    pipenv install
    ```
  - Run the project using the pip enviroment:
    ```
    pipenv run python run.py
    ```

### Usefull notes
  - Python version: 3.7.4

## Check functionality

### API

For the purposes of the project, as a reference and interaction point is used the Swagger which is provided through the library which was used for the general API implementation. You can access to this
location by visiting http://127.0.0.1:5000/doc/. Subsequently, you will be able to see three (3) main entities. The first two of them are reffered to the end-points of the application, where you can interact by inserting suitable data if needed and/or click for the request. At this point, i would like to mention that the second one, "Campaign", as you will also see, is my approach to the Campaign mock API. The third one is a model which describes the input that bid request have to contains. Lastly, you can take a look of the full API description by visiting http://127.0.0.1:5000/api/swagger.json.

#### Usefull notes
- Check log file for tracking of the API behaviour.

### TEST

- Change to src/main/tests directory.

- Run the tests using:
    ```
    pytest
    ```

#### Usefull notes
- The server must be running.
