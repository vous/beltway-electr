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
	nation = ForeignKeyField(Nation, "states")
	abbreviation = CharField()

class County(BaseModel):
	name = CharField()
	state = ForeignKeyField(State, "counties")
	abbreviation = CharField()

class Municipality(BaseModel):
	name = CharField()
	county = ForeignKeyField(County, "municipalities")

class NationalLeader(BaseModel):
	title = CharField()
	nation = ForeignKeyField(Nation, "leader")

class StateLeader(BaseModel):
	title = CharField()
	state = ForeignKeyField(State, "leader")

class CountyLeader(BaseModel):
	title = CharField()
	county = ForeignKeyField(County, "leader")

class MunicipalityLeader(BaseModel):
	title = CharField()
	county = ForeignKeyField(Municipality, "leader")

class NationalLegislature(BaseModel):
	# Not the legislator, the Congress!
	name = CharField()
	nation = ForeignKeyField(Nation, "legislature")

class StateLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(State, "legislature")

class CountyLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(County, "legislature")

class MunicipalityLegislature(BaseModel):
	name = CharField()
	state = ForeignKeyField(Municipality, "legislature")

class NationalLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # Officeholder's title
	name = CharField() # i.e. AK-AL or NY-1
	# Organized by state
	state = ForeignKeyField(State, "national_seats")
	# Some seats may become inactive due to population shifts
	active = BooleanField(default = True)

class StateLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by county
	county = ForeignKeyField(County, "state_seats")
	# Some seats may become inactive due to population shifts
	active = BooleanField(default = True)

class CountyLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by county
	county = ForeignKeyField(County, "county_seats")
	# Some seats may become inactive due to legislative actions
	active = BooleanField(default = True)

class MunicipalityLegislator(BaseModel):
	# Not the person, the office
	title = CharField() # officeholder's title
	name = CharField() # i.e. NY-1 or WC-2
	# Organized by municipality
	municipality = ForeignKeyField(Municipality, "municipality_seats")
	# Some seats may become inactive due to legislative actions
	active = BooleanField(default = True)