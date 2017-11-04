import flask

app = flask.Flask('myapp')

@app.route("/")
def index():
    return flask.render_template('splash.html', text='Hello world')

@app.route("/user/<name>")
def hello_user(name):
    text = 'Hello, {}'.format(name)
    return flask.render_template('splash.html', text=text)

if __name__ == '__main__':
    app.run()
