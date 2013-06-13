from peewee import *

#######################
# Setup
db = SqliteDatabase('beltway.db')
#######################

class BaseModel(Model):
	class Meta:
		database = db

class Nation(BaseModel):
	name = CharField()

class State(BaseModel):
	name = CharField()
	nation = ForeignKeyField(Nation, related_name = "states")
	abbreviation = CharField()

class County(BaseModel):
	name = CharField()
	state = ForeignKeyField(State, related_name = "counties")
	abbreviation = CharField()

class Municipality(BaseModel):
	name = CharField()
	county = ForeignKeyField(County, related_name = "municipalities")

class NationalLeader(BaseModel):
	title = CharField()
	nation = ForeignKeyField(Nation, related_name = "leader")

class StateLeader(BaseModel):
	title = CharField()
	state = ForeignKeyField(State, related_name = "leader")

class CountyLeader(BaseModel):
	title = CharField()
	county = ForeignKeyField(County, related_name = "leader")

class MunicipalityLeader(BaseModel):
	title = CharField()
	county = ForeignKeyField(Municipality, related_name = "leader")

class NationalLegislature(BaseModel):
	# Not the legislator, the Congress!
	name = CharField()
	nation = ForeignKeyField(Nation, related_name = "legislature")

class StateLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(State, related_name = "legislature")

class CountyLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(County, related_name = "legislature")

class MunicipalityLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(Municipality, related_name = "legislature")

class NationalLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # Officeholder's title
	name = CharField() # i.e. AK-AL or NY-1
	# Organized by state
	state = ForeignKeyField(State, related_name = "national_seats")
	# Some seats may become inactive due to population shifts
	active = BooleanField(default = True)
	next_election = DateField() # When is the next election in this seat?

class StateLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by county
	county = ForeignKeyField(County, related_name = "state_seats")
	# Some seats may become inactive due to population shifts
	active = BooleanField(default = True)
	next_election = DateField() # When is the next election in this seat?

class CountyLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by county
	county = ForeignKeyField(County, related_name = "county_seats")
	# Some seats may become inactive due to legislative actions
	active = BooleanField(default = True)
	next_election = DateField() # When is the next election in this seat?

class MunicipalityLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by municipality
	municipality = ForeignKeyField(Municipality, related_name = "municipality_seats")
	# Some seats may become inactive due to legislative actions
	active = BooleanField(default = True)
	next_election = DateField() # When is the next election in this seat?

class StateParty(BaseModel):
	# The party itself
	#### THERE SHOULD BE A REFERENCE TO THE USER
	name = CharField()
	status = IntegerField() # 1 - unrecognized state, 2 = recognized state
	funds = DecimalField(decimal_places = 2)
	state = ForeignKeyField(State, related_name = "parties") # What states it is open in 

class NationalParty(BaseModel):
	# The party itself
	#### THERE SHOULD BE A REFERENCE TO THE USER
	name = CharField()
	status = IntegerField() # 1 - unrecognized state, 2 = recognized state
	funds = DecimalField(decimal_places = 2)
	nation = ForeignKeyField(Nation, related_name = "parties") # What states it is open in 

class Politician(BaseModel):
	name = CharField()
	funds = DecimalField(decimal_places = 2)
	national_party = ForeignKeyField(NationalParty, related_name = "politicians")
	state_party = ForeignKeyField(StateParty, related_name = "politicians")
	econ_freedom = DecimalField(decimal_places = 2)
	civil_freedom = DecimalField(decimal_places = 2)

class MunicipalityLegislatorPerson(Politician):
	office = ForeignKeyField(MunicipalityLegislator, related_name = "politician")

class CountyLegislatorPerson(Politician):
	office = ForeignKeyField(CountyLegislator, related_name = "politician")

class StateLegislatorPerson(Politician):
	office = ForeignKeyField(StateLegislator, related_name = "politician")

class NationalLegislatorPerson(Politician):
	office = ForeignKeyField(NationalLegislator, related_name = "politician")


def create_all_tables():
	NationalLegislatorPerson.create_table()	
	StateLegislatorPerson.create_table()
	CountyLegislatorPerson.create_table()
	MunicipalityLegislatorPerson.create_table()
	NationalParty.create_table()
	StateParty.create_table()
	MunicipalityLegislator.create_table()
	CountyLegislator.create_table()
	StateLegislator.create_table()
	NationalLegislator.create_table()
	MunicipalityLegislature.create_table()
	CountyLegislature.create_table()
	StateLegislature.create_table()
	NationalLegislature.create_table()
	Municipality.create_table()
	County.create_table()
	State.create_table()
	Nation.create_table()