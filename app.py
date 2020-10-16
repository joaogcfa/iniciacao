from flask import Flask, render_template, url_for, request, redirect
import tobii_research as tr
import time
from datetime import datetime
import pyrebase
import sys

found_eyetrackers = tr.find_all_eyetrackers()

print(found_eyetrackers)
my_eyetracker = None

for i in found_eyetrackers:
    if i.model[:2] == "X2": #"X2":
        my_eyetracker = i

if my_eyetracker == None:
    sys.exit()

print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    #print("funcao")
    gaze_left_eye=gaze_data['left_gaze_point_on_display_area']
    gaze_right_eye=gaze_data['right_gaze_point_on_display_area']
    print("Left eye: ({0}) \t Right eye: ({1})".format(gaze_left_eye, gaze_right_eye))

my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

def timeSyncCallback(self, timeSyncData):
    print("AAA")

my_eyetracker.subscribe_to(tr.EYETRACKER_TIME_SYNCHRONIZATION_DATA,
                                     timeSyncCallback,
                                     as_dictionary=True)

time.sleep(50)
# my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

# config = {
#     "apiKey": "AIzaSyDLYrb2MHSNe2kP3Te7RVNnnxne-g2QV20",
#     "authDomain": "iniciacaoeyetracking.firebaseapp.com",
#     "databaseURL": "https://iniciacaoeyetracking.firebaseio.com",
#     "projectId": "iniciacaoeyetracking",
#     "storageBucket": "iniciacaoeyetracking.appspot.com",
#     "messagingSenderId": "508624071073",
#     "appId": "1:508624071073:web:7a8d981b0903297a0b83e0"

# }

# firebase = pyrebase.initialize_app(config)

# db = firebase.database()

# # db.child("usuarios").push({"horario":{"x":"posicao x", "y":"posicao y"}})
# app = Flask(__name__)


# @app.route('/')
# def test_page():
#     # look inside `templates` and serve `index.html`
#     return render_template('index.html')

# @app.route('/hello', methods=['POST'])
# def hello():
#     if request.method == 'POST':
#         print('Incoming..')
#         # print(request.get_json())
#         html = request.get_json()
        
#         for tempo in html:
#             time_stamp_html = tempo
#             posicoes = html[tempo]
#             print("para o tempo {}".format(time_stamp_html))
#             for itens in posicoes:
#                 if itens == "y":
#                     print("y: ", posicoes[itens])
#                     y= posicoes[itens]
#                 else:
#                     print("x: ", posicoes[itens])
#                     x = posicoes[itens]
#             db.child("usuarios").child("primeiro").push({time_stamp_html:{"x":x, "y":y}})



#         #     min_position_html = html[tempo]
#         #     max_position_html = min_position_html
#         return 'OK', 200


# if __name__ == "__main__":
#     app.run(debug=True)