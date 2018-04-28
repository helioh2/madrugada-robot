import bluetooth
import math

#Look for all Bluetooth devices
#the computer knows about.
print("Searching for devices...")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print(num , ": " , bluetooth.lookup_name( i ))

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = input("> ") - 1
print("You have selected", bluetooth.lookup_name(nearby_devices[selection]))
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

	def calcDxDy(self, distance, angle):
		angle_rad = math.radians(angle)
		dx = distance * math.cos(angle_rad)
		dy = distance * math.sin(angle_rad)
		return dx, dy

	def forward(self, distance):

		dx, dy = calcDxDy(distance, self.angle)

		#Updating internal state
		self.x += dx;
		self.y += dy;

		#Building command
		data = "M " + str(dx) + " " + str(dy)
		print(data)

		#Sending command
		self.sock.send(data)

	def backward(self, distance):

		inverted_angle = (self.angle + 180) % 360
		dx, dy = calcDxDy(distance, inverted_angle)

		#Updating internal state
		self.x += dx;
		self.y += dy;

		#Building command
		data = "M " + str(dx) + " " + str(dy)
		print(data)

		#Sending command
		self.sock.send(data)

	def turn(self, angle):
		self.angle = (self.angle + angle) % 360
		print(self.angle)

		def pen_up(self):
			self.pen_is_down = False

		#Building command
		data = "U"
		print(data)

		#Sending command
		self.sock.send(data)

	def pen_down(self):
		self.pen_is_down = True

		#Building command
		data = "D"
		print(data)

		#Sending command
		self.sock.send(data)

	def go_to(self, x, y):
		self.x = x
		self.y = y

		#Building command
		data = "G " + str(self.x) + " " + str(self.y)
		print(data)

		#Sending command
		self.sock.send(data)



#tests:
turtle = Turtle()
turtle.pen_down()
turtle.forward(50)
turtle.turn(90)
turtle.forward(50)
turtle.pen_up()
turtle.go_to(0,0)




