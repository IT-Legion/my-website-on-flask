from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    return 'Привет, Мир!'


@app.route('/about')
def maks():

    return 'Это Flask детка!'


if __name__ == '__main__':
    app.run(debug=True)