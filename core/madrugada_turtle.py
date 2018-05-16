
import bluetooth
import math
import time


class BluetoothConnection:

	def getInfo(self):
		return self.bd_addr, self.port

	def getNearbyDevices(self):
		return bluetooth.discover_devices()

	def selectDevice(self, device_addr):
		self.bd_addr = device_addr
		self.port = 1

	def setupOnTerminal(self):
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

class BluetoothSocketMock():

    def send(self, data):
        print("Teste enviando ao bluetooth:", data)

class MadrugadaTurtle:

	def __init__(self, sock, 
		xlimits = (-150, 150), 
		ylimits = (-100, 100)):
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

	def forward(self, distance=0):

		dx, dy = self.calcDxDy(distance, self.angle)
		dx, dy = math.floor(dx), math.floor(dy)

		if not self.inLimits(self.x + dx, self.y + dy): return

		#Updating internal state
		self.x += dx
		self.y += dy

		#Building command
		data = "M " + str(dx) + " " + str(dy)
		print(data)

		#Sending command
		time.sleep(max(abs(dx), abs(dy))/10)
		self.sock.send(data+"#")

	def backward(self, distance=0):

		inverted_angle = (self.angle + 180) % 360
		dx, dy = self.calcDxDy(distance, inverted_angle)
		dx, dy = math.floor(dx), math.floor(dy)

		if not self.inLimits(self.x + dx, self.y + dy): return

		#Updating internal state
		self.x += dx
		self.y += dy

		#Building command
		data = "M " + str(dx) + " " + str(dy)
		print(data)

		#Sending command
		time.sleep(max(abs(dx), abs(dy))/10)
		self.sock.send(data+"#")

	def turn(self, angle=0):
		self.angle = (self.angle + angle) % 360
		print(self.angle)

	def turn_right(self, angle=0):
		self.turn(-angle)

	def turn_left(self, angle=0):
		self.turn(angle)

	def pen_up(self):
		self.pen_is_down = False

		#Building command
		data = "U"
		print(data)

		#Sending command
		time.sleep(1)
		self.sock.send(data+"#")

	def pen_down(self):
		self.pen_is_down = True

		#Building command
		data = "D"
		print(data)

		#Sending command
		time.sleep(1)
		self.sock.send(data+"#")

	def go_to(self, x=0, y=0):
		if not self.inLimits(x, y): return
		time.sleep(max(abs(self.x), abs(self.y))/10)

		self.x = x
		self.y = y

		#Building command
		data = "G " + str(self.x) + " " + str(self.y)
		print(data)

		#Sending command
		self.sock.send(data+"#")




