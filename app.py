from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True)