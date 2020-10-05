from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyrebase

config = {
    "apiKey": "AIzaSyDLYrb2MHSNe2kP3Te7RVNnnxne-g2QV20",
    "authDomain": "iniciacaoeyetracking.firebaseapp.com",
    "databaseURL": "https://iniciacaoeyetracking.firebaseio.com",
    "projectId": "iniciacaoeyetracking",
    "storageBucket": "iniciacaoeyetracking.appspot.com",
    "messagingSenderId": "508624071073",
    "appId": "1:508624071073:web:7a8d981b0903297a0b83e0"

}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("usuarios").push({"horario":{"x":"posicao x", "y":"posicao y"}})
app = Flask(__name__)


@app.route('/')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    if request.method == 'POST':
        print('Incoming..')
        # print(request.get_json())
        html = request.get_json()
        
        for tempo in html:
            time_stamp_html = tempo
            posicoes = html[tempo]
            print("para o tempo {}".format(time_stamp_html))
            for itens in posicoes:
                if itens == "y":
                    print("y: ", posicoes[itens])
                    y= posicoes[itens]
                else:
                    print("x: ", posicoes[itens])
                    x = posicoes[itens]
            db.child("usuarios").child("primeiro").push({time_stamp_html:{"x":x, "y":y}})



        #     min_position_html = html[tempo]
        #     max_position_html = min_position_html
        return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True)