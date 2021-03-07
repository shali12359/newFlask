from flask import Flask, request 
import random

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # GET AUDIO FILE & SAVE 
    # audio = request.files['audio']
    # fileName = str(random.randint(0, 100000)) 
    # audio.save(fileName)
     
    # MAKE PREDICTION 

    # REMOVE AUDIO FILE 

    # SEND BACK PREDICTION 
    return "seven"