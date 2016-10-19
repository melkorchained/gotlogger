
class Board:

	def territories():
		land = {'Castle Black':{'Power':1},
				'Karhold':{'Power:1'},
				'The Stony Shore':{'Supply:1'},
				'White Harbor':{'Castle':True}
				'Widow\'s Watch':{'Supply':1},
				'Winterfell':{'Stronghold':True, 'Power':1, 'Supply':1, 'Garrison':True},
				'Moat Cailin':{'Castle':True},
				'Greywater Watch':{'Supply':1},
				'Flint\'s Finger': {'Castle':True},
				'Seagard':{'Stronghold':True,'Supply':1,'Power':1},
				'The Twins':{'Power':1},
				'The Fingers':{'Supply':1},
				'The Mountains of the Moon':{'Supply':1},
				'The Eyrie':{'Power':1,'Castle':True,'Supply':1},
				'Riverrun':{'Stronghold':True,'Power':1,'Supply':1},
				'Lannisport':{'Stronghold':True, 'Garrison':True,'Supply':2}
				'Stoney Sept':{'Power':1},
				'Harrenhal':{'Castle':True,'Power':1},
				'Cracklaw Point':{'Castle':True},
				'Dragonstone':{'Supply':1,'Power':1,'Stronghold':True,'Garrison':True},
				'King\'s Landing':{'Stronghold':True,'Power':2},
				'Kingswood':{'Power':1,'Supply':1},
				'Storm\'s End':{'Castle':True},
				'The Boneway':{'Power':1},
				'Yronwood':{'Castle':True},
				'Sunspear':{'Stronghold':True, 'Garrison':True,'Power':1,'Supply':1},
				'Salt Shore':{'Supply':1},
				'Starfall':{'Castle':True,'Supply':1},
				'Prince\'s Pass':{'Power':1, 'Supply':1},
				'Three Towers':{'Supply':1},
				'The Arbor':{'Power':1},
				'Oldtown':{'Stronghold':True},
				'Dornish Marches':{'Power':1},
				'The Reach':{'Castle':True},
				'Highgarden':{'Stronghold':True,'Garrison':True,'Supply':2},
				'Searoad Marshes':{'Supply':1},
				'Blackwater':{'Supply':2}}

		units = {}

		sea_connect = {}

		land_connect = {}