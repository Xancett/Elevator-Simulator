class Elevator:
	def __init__(self, floors):
		self.floors = floors
		self.location = 0
	def getLocation(self):
		return self.location