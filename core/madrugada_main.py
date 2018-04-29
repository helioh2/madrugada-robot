from core.madrugada_turtle import *

test = True

if test:
    sock = BluetoothSocketMock()
    turtle = MadrugadaTurtle(sock)
else: 
    bd_connection = BluetoothConnection()
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect(bd_connection.getInfo())
    turtle = MadrugadaTurtle(sock)

def execute(code):
    turtle.pen_up()
    turtle.go_to(0,0)
    turtle.pen_down()
    exec(code)




