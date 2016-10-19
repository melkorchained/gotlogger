class Territory(object):

	def __init__(self, castle, stronghold, power, supply, port, garrison):
		self.castle = castle
		self.stronghold = stronghold
		self.power = power
		self.supply = supply
		self.port = port
		self.garrison = garrison
		self.adjacent_sea = []
		self.adjacent_land = []
		self.land_by_sea = []
		if self.castle and self.stronghold:
			raise "Invalid entry, a territory cannot possess both a castle and a stronghold"

	def current_strength(self):
		pass

	def current_units(self):
		pass

	def mustering():
		if self.castle:
			return 1
		elif self.stronghold:
			return 2
		else:
			return 0

	def muster_units(self, muster_call):
		pass

class Winterfell(Territory):

	def __init__(self):
		Territory.__init__(self, False, True, 1, 1, True, True)
		self.garrison_strength = 2
