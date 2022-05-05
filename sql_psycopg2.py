"""
Imports the psycopg2 library
"""
import psycopg2


# Connect to 'Chinook' database - this is also where local host,
# username & password would be added if required
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
# A cursor object another way of saying a set or list
# - similar to an array in JavaScript
# Anything that we query in the database becomes part of the cursor
cursor = connection.cursor()

# QUERIES GO HERE - after the cursor has been defined but
# before results fetched

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# %s is a python string placeholder - you then define the
# desired string within a list ["desired string"]
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with the "ArtistId" #51
# on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen"
# from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Fetch the results (used to fetch multiple records)
results = cursor.fetchall()

# Fetch the result (used to fetch a single record)
# results = cursor.fetchone()

# Once the results have been fetched we need to Close the connection
# to the database
connection.close()

# Print results
# as the cursor object stores results similar to an array in JavaScript
# we need to iterate over the results with a for loop to be able to
# access the results individually
for result in results:
    print(result)
