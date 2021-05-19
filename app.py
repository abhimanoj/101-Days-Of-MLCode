import os
from flask import Flask
from .numpy_py import NumpyOperation


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():

    
    return "Test Result"


@app.route("/numpy")
def numpy():

    arr_data_1 = [1, 2, 3]


    arr_data_2 = [
                [1, 2, 3],
                [4, 5, 6]
                ]
    p1 = NumpyOperation(arr_data_1, arr_data_2)

    
    return "Test Result"


if __name__ == '__main__':

    app.secret_key = app.config.get("SECRET_KEY")
    app.run(debug=True)