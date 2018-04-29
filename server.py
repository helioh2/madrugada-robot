from flask import Flask, request, url_for, redirect
from core.madrugada_main import *
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))

@app.route('/executeCode', methods=['POST'])
def executeCode():
    code = request.get_data() 
    print(code)
    execute(code)
    return 'ok'



