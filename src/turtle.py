import bluetooth
import math

#Look for all Bluetooth devices
#the computer knows about.
print "Searching for devices..."
print ""
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print "Select your device by entering its coresponding number..."
for i in nearby_devices:
	num+=1
	print num , ": " , bluetooth.lookup_name( i )

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = input("> ") - 1
print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
bd_addr = nearby_devices[selection]

port = 1

class Turtle:

	x = 0
	y = 0
	pen_is_down = True
	angle = 0

	sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

	def __init__(self):
		#Connect to the bluetooth device
    	#and initialize the GUI
        self.sock.connect((bd_addr, port))

    def forward(self, distance):
    	float x, y;
    	#Updating internal state
		self.angle = (self.angle * math.pi) / 180;
		self.x = distance * math.cos(self.angle);
		self.y = distance * math.sin(self.angle);

		#Building command
		data = "M " + str(self.x) + " " + str(self.y)

		#Sending command
		self.sock.send(data)

	def turn(self, angle):
		self.angle = (self.angle + angle) % 360

	def pen_up(self):
		self.pen_is_down = False

		#Building command
		data = "U"

		#Sending command
		self.sock.send(data)

	def pen_down(self):
		self.pen_is_down = True

		#Building command
		data = "D"

		#Sending command
		self.sock.send(data)

	def go_to(self, x, y):
		self.x = x
		self.y = y

		#Building command
		data = "G " + str(self.x) + " " + str(self.y)

		#Sending command
		self.sock.send(data)








