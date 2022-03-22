from flask import Flask, request, jsonify, render_template
import os
import requests
import json
import requests
import re
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
        
    message = request.form['message']
    params = {
        "message":message
    }

    data = requests.post("http://localhost:5005/webhooks/rest/webhook", json=params)
    response = data.json()
    
    response_text = { "message": response }
                        
    return jsonify(response_text)
    
# run Flask app
if __name__ == "__main__":
    app.run(port = '5000')
