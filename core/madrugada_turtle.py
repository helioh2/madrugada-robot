
import bluetooth
import math


class BluetoothConnection:

	def __init__(self):
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
		self.bd_addr = nearby_devices[selection]
		self.port = 1

	def getInfo(self):
		return self.bd_addr, self.port

class MadrugadaTurtle:

	def __init__(self, sock, 
		xlimits = (-200, 200), 
		ylimits = (-150, 150)):
		self.x = self.y = self.angle = 0
		self.pen_is_down = True
		self.xlimits = xlimits
		self.ylimits = ylimits #experimental (ajustar)

		self.sock = sock
		
	def calcDxDy(self, distance, angle):
		angle_rad = math.radians(angle)
		dx = distance * math.cos(angle_rad)
		dy = distance * math.sin(angle_rad)
		return dx, dy

	def inLimits(self, x, y):
		return self.xlimits[0] <= x <= self.xlimits[1] \
				and self.ylimits[0] <= y <= self.ylimits[1]

	def forward(self, distance):

		dx, dy = self.calcDxDy(distance, self.angle)

		if not self.inLimits(self.x + dx, self.y + dy): return

		#Updating internal state
		self.x += dx
		self.y += dy

		#Building command
		data = "M " + str(dx) + " " + str(dy)
		print(data)

		#Sending command
		self.sock.send(data)

	def backward(self, distance):

		inverted_angle = (self.angle + 180) % 360
		dx, dy = self.calcDxDy(distance, inverted_angle)

		if not self.inLimits(self.x + dx, self.y + dy): return

		#Updating internal state
		self.x += dx
		self.y += dy

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
		if not self.inLimits(x, y): return

		self.x = x
		self.y = y

		#Building command
		data = "G " + str(self.x) + " " + str(self.y)
		print(data)

		#Sending command
		self.sock.send(data)

# #tests:
# bd_connection = BluetoothConnectionReal()
# sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# sock.connect(bd_connection.getInfo())

# turtle = Turtle(bd_connection)
# turtle.pen_down()
# turtle.forward(50)
# turtle.turn(90)
# turtle.forward(50)
# turtle.pen_up()
# turtle.go_to(0,0)




