from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def main_page():
    return render_template('GLAVNYA.html')

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')