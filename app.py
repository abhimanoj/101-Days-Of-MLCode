import os
from flask import Flask
from numpy_py.numpy_core import NumpyOperation
from numpy_py.numpy_tutorial import NumpyTutorial

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

import random

@app.route("/")
def index():
    #operation
    #data is loaded
    #file is loaded

    #Result
    return "Test Result"

@app.route("/numpy")
def numpy():

    arr_data_1 = [1, 2, 3]


    arr_data_2 = [
                [1, 2, 3],
                [4, 5, 6]
                ]
    np_op = NumpyOperation(arr_data_1, arr_data_2)

    
    return  np_op.__str__()


@app.route("/numpy_tutorial")
def numpy_tutorial():

  
    np_mul = NumpyTutorial()
    
    
    return  np_mul.operation().__str__()


if __name__ == '__main__':

    app.secret_key = app.config.get("SECRET_KEY")
    app.run(debug=True)