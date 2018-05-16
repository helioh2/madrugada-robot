from core.madrugada_turtle import *
import threading

bd_connection = BluetoothConnection()

# Mock socket by default:
sock = BluetoothSocketMock()
turtle = MadrugadaTurtle(sock)

# bd_connection.setupOnTerminal()
# sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# print(sock)
# print(bd_connection.getInfo())
# x = sock.connect(bd_connection.getInfo())  #verificar erro de conexao
# print(x)
# turtle = MadrugadaTurtle(sock)

def loadDevices():
    return bd_connection.getNearbyDevices()

def setupDevice(device_addr):
    bd_connection.selectDevice(device_addr)

    #create and inject socket
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    print(sock)
    print(bd_connection.getInfo())
    x = sock.connect(bd_connection.getInfo())  #verificar erro de conexao
    print(x)
    global turtle
    turtle = MadrugadaTurtle(sock)

def execute(code):
    def real_execute():
        turtle.pen_up()
        turtle.go_to(0,0)
        turtle.angle = 0
        turtle.pen_down()
        exec(code)
    t = threading.Thread(target=real_execute)
    t.start()
    





