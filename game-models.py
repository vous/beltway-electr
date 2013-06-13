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

class County(BaseModel):
	name = CharField()
	state = ForeignKeyField(State, "counties")

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