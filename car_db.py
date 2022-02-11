import sqlite3
import csv

conn = sqlite3.connect("car.db")
cursor = conn.cursor()

# 1- creating table columns
#cursor.execute("""CREATE TABLE car (
#    name text,
#    mpg float,
#    cylinders integer,
#    displacement float,
#    horsepower float,
#    weight float,
#    acceleration float,
#    model integer,
#    country text)""")

#print("Car table created")

# 2 - Writing read data from csv-file
#with open(f"cars.csv", "r", encoding="utf-8") as file:
#    csv_reader = csv.reader(file, delimiter=";")
#    columns = next(csv_reader)
#    for line in csv_reader:
#        cursor.execute("INSERT INTO car "
#                       "(name, mpg, cylinders, displacement, horsepower, "
#                       "weight, acceleration, model, country) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?)", line)

#cursor.execute("SELECT rowid, * FROM car")

#cursor.execute("SELECT * FROM car WHERE country = 'US'")
#cursor.execute("SELECT * FROM car WHERE country = 'Japan'")
#cursor.execute("SELECT * FROM car WHERE country = 'Europe'")

items = cursor.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()
