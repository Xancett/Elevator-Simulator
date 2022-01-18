from audioop import reverse
import math
import threading
class Elevator:
	def __init__(self, floors):
		self.floors = floors
		self.location = 0
		self.up_queue = [floors]
		self.down_queue = [floors]
		self.direction = 0
		self.UpdatePosition()
	def getLocation(self):
		return self.location
	def PushButton(self, up, floor):
		if (up):
			self.up_queue.append(floor)
		else:
			self.down_queue.append(floor)
		if (self.direction == 0):
			self.direction = 1 if up else -1
	def ChooseFloor(self, floor):
		print("Picked a floor")
	def UpdatePosition(self):
		threading.Timer(5.0, self.UpdatePosition).start()
		self.CheckDirection()
		if (self.direction == 1):
			if (len(self.up_queue) > 0):
				self.up_queue.sort()
				self.location = self.up_queue.pop()
				print("Now on floor ", self.location)
		if (self.direction == -1):
			if (len(self.down_queue) > 0):
				self.down_queue.sort(reverse=True)
				self.location = self.down_queue.pop()
				print("Now on floor ", self.location)
	def CheckDirection(self):
		checkqueue = self.up_queue if self.direction == 1 else self.down_queue
		for floor in checkqueue:
			if math.copysign(1, floor - self.location) == self.direction:
				return
		self.direction *= -1