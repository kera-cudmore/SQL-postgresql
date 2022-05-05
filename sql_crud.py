"""
Imports the following modules from the sqlalchemy library
"""
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "Chinook" database
db = create_engine("postgresql:///chinook")
# the base class grabs the metadata that is produced by
# our database table schema and creates a subclass to map
# everything back to us in the base variable
base = declarative_base()


# create a class-based model for the "Programmer" table
"""
Class-based model for Programmer table - extends from the base
"""
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connection to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our "Programmer" table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

kera_cudmore = Programmer(
    first_name="Kera",
    last_name="Cudmore",
    gender="F",
    nationality="British",
    famous_for="Learning to Code"
)

# add each instance of our programmers to our session
# IMPORTANT - comment out ones that have already been committed
# otherwise you will end up with double entries
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(kera_cudmore)


# commit our session to the database - for adding above records
# session.commit()


# UPDATING A SINGLE RECORD
# using .first() prevents having to use a for loop to loop over
# all the entries even though there is only 1 record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"


# commit our session to the database - for updating the entry
# the commit session needs to come after the info you are updating
# session.commit()


# UPDATING MULTIPLE RECORDS
# adding all records from the Programmer table to a variable
# using for loop to look at each record and change them
# the session.commit() needs to be part of the loop to commit the changes
#people = session.query(Programmer)
#for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else:
#        print("Gender not defined")
#    session.commit()


# DELETING A SINGLE RECORD
#fname = input("Enter a first name: ")
#lname = input("Enter a last name: ")
#programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
#if programmer is not None:
#    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#    confirmation = input("Are you sure you want to delete this record? (y/n) ")
#    if confirmation.lower() == "y":
#        session.delete(programmer)
#        session.commit()
#        print("Programmer has been deleted")
#    else:
#        print("Programmer not deleted")
#else:
#    print("No records found")


# !! THIS CODE IS FOR DEMO ONLY DO NOT RUN !!
# DELETE MULTIPLE RECORDS
# IF USING IN THE REAL WORLD MAKE SURE TO USE DEFENSIVE PROGRAMMING 
# TO MAKE SURE THAT DELETING ALL RECORDS IS WHAT IS REQUIRED
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
