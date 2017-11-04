import flask

app = flask.Flask('myapp')

@app.route("/")
def index():
    return 'Hello world'

@app.route("/user/<name>")
def hello_user(name):
    return 'Hello, {}'.format(name)


if __name__ == '__main__':
    app.run()
