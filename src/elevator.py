from audioop import reverse
import math
import threading
class Elevator:
	def __init__(self, floors):
		self.floors = floors
		self.location = 1
		self.up_queue = []
		self.down_queue = []
		self.direction = 0
		self.UpdatePosition()
	def getLocation(self):
		return self.location
	def PushButton(self, up, floor):
		if (floor < 0 or floor > self.floors):
			return
		if (up):
			self.up_queue.append(floor)
		else:
			self.down_queue.append(floor)
		if (self.direction == 0):
			self.direction = 1 if up else -1
	def ChooseFloor(self, floor):
		if (floor < 0 or floor > self.floors):
			return
		if (floor > self.location):
			self.up_queue.append(floor)
			self.direction = 1 if self.direction == 0 else self.direction
		if (floor < self.location):
			self.down_queue.append(floor)
			self.direction = -1 if self.direction == 0 else self.direction
	def UpdatePosition(self):
		threading.Timer(5.0, self.UpdatePosition).start()
		self.CheckDirection()
		if (self.direction == 1):
			if (len(self.up_queue) > 0):
				self.up_queue.sort(reverse=True)
				self.location = self.up_queue.pop()
		if (self.direction == -1):
			if (len(self.down_queue) > 0):
				self.down_queue.sort()
				self.location = self.down_queue.pop()
		try:
			self.gui.UpdateElevatorLocation(self.location)
		except:
			pass
	def CheckDirection(self):
		checkqueue = self.up_queue if self.direction == 1 else self.down_queue
		for floor in checkqueue:
			if math.copysign(1, floor - self.location) == self.direction:
				return
		self.direction *= -1
		if len(self.up_queue) == 0 and len(self.down_queue) == 0:
			self.direction = 0
	def PassGUI(self, gui):
		self.gui = gui