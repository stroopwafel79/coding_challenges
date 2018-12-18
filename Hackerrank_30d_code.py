# Day one:
class Car():

	def __init__(self, max_speed, min_speed, weight, condition, is_on=False,):
		self.max_speed = max_speed
		self.min_speed = min_speed
		self.weight = weight
		self.condition = condition
		self.is_on = is_on

	def print_values(self):
		print(f"max_speed: {self.max_speed}")

prius = Car(200, 0, 5000, "Great")
prius.print_values()



