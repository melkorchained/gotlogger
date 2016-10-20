
class Territory(object):
	'''
	Class describing a territory. Each territory can possess either Power, Supply, both, or neither
	In addition, a territory can possess either a castle or a stronghold, and a port
	A territory has a garrison if:
	a) It is a House's starting capital
	b) It is a specially reinforced territory (eg: King's Landing, The Eyrie)
	
	A territory loses its garrison if it is defeated, and doesn't regain it for the remainder of the game

	The following externally usable methods will be contained in this class:

	current_strength: Returns the combat strength of the territory

	current_units: Returns all units in the territory as a tuple

	supporting_units: returns all units supporting this territory

	order_token: returns the order token placed on the territory as a string, int tuple
	'''

	current_owner = ""
	def __init__(self, castle, stronghold, power, supply, port, garrison, terrain):
		self.castle = castle
		self.stronghold = stronghold
		self.power = power
		self.supply = supply
		self.port = port
		self.garrison = garrison
		self.adjacent_sea = []
		self.adjacent_land = []
		self.terrain = terrain		#can be land or sea

	def current_strength(self, combat_status, order, enemy):
		units = self.current_units()
		if self.terrain == "Land":
			strength = (units[0]*1)+(units[1]*2)
		elif self.terrain == "Sea":
			strength = units[3]*1
		if combat_status == "Attacking":
			if enemy.castle or enemy.stronghold:
				strength += units[2]*4
			if self.order_token()[0] == "March":
				strength += self.order_token()[1]
		#COMPLETE DEFENSIVE STRENGTH
		return strength

	def current_units(self):
		pass

	def supporting_units(self):
		pass

	def order_token(self):
		pass

	@staticmethod
	def mustering_strength():
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
