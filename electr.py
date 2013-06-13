from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello_world(name="World"):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.debug = True
    app.run()