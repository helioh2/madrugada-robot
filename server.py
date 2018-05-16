from flask import Flask, request, url_for, redirect, jsonify
import core.madrugada_main as madrugada
app = Flask(__name__)
# app.run(debug=True)

@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))

@app.route('/executeCode', methods=['POST'])
def executeCode():
    code = request.get_data() 
    print(code)
    madrugada.execute(code)
    return 'ok'

@app.route('/loadDevices')
def loadDevices():
    devices = madrugada.loadDevices()
    print(devices)
    return jsonify(devices)

@app.route('/setDevice')
def setDevice():
    bd_addr = request.args.get('bdaddr')
    madrugada.setupDevice(bd_addr) #pode dar erro, fazer verificacao
    return 'ok'

@app.route('/getAngle')
def getAngle():
    return str(madrugada.turtle.angle)