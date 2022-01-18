import threading
class Elevator:
	def __init__(self, floors):
		self.floors = floors
		self.location = 0
		self.queue = [floors]
		self.UpdatePosition()
	def getLocation(self):
		return self.location
	def PushButton(self, up, floor):
		print("Pushed button")
		print("Request on floor ", floor)
		self.queue.append(floor)
	def ChooseFloor(self, floor):
		print("Picked a floor")
	def UpdatePosition(self):
		threading.Timer(5.0, self.UpdatePosition).start()
		if len(self.queue) > 0:
			self.location = self.queue.pop()
			print("Now on floor ", self.location)