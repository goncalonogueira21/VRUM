from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
	# setting debug to True enables hot reload
	# and also provides a debuger shell
	# if you hit an error while running the server
	app.run(debug = True)
