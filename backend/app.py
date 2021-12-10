import jwt

from flask import Flask
from flask import request, jsonify, make_response
from functools import wraps
from secretsFolder import secrets

app = Flask(__name__)
app.debug = True


if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debuger shell
    # if you hit an error while running the server
    app.run(debug=True)
