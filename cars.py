import csv
import json

formatfile_list = ["txt", "csv", "json"]

formatfile = input("Enter the file format for saving data: txt, csv or json: ")

if formatfile not in formatfile_list:
    print("You entered the wrong file format")
    exit(0)

car_us_list = []
car_europe_list = []
car_japan_list = []

with open(f"cars.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    header = next(csv_reader)

    for line in csv_reader:
        if "US" in line:
            car_us_list.append(line)
            car_us_list.sort(key=lambda x: x[0])

        elif "Europe" in line:
            car_europe_list.append(line)
            car_europe_list.sort(key=lambda x: x[0])

        elif "Japan" in line:
            car_japan_list.append(line)
            car_japan_list.sort(key=lambda x: x[0])

with open(f"fileus.{formatfile}", "w", encoding="utf-8") as cars_file:
    for car in car_us_list:
        car_us = tuple(car)
        if formatfile == "txt":
            car = " ".join(car) + "\n"
            txt_file = cars_file.write(car)

        elif formatfile == "csv":
            csv_file = csv.writer(cars_file, dialect="excel")
            csv_file.writerow(car_us)

        elif formatfile == "json":
            json_file = json.dump(car_us_list, cars_file, indent=4)

with open(f"fileeurope.{formatfile}", "w", encoding="utf-8") as cars_file:
    for car in car_europe_list:
        car_europe = tuple(car)
        if formatfile == "txt":
            car = " ".join(car) + "\n"
            cars_file.write(car)

        elif formatfile == "csv":
            csv_file = csv.writer(cars_file, dialect="excel")
            csv_file.writerow(car_europe)

        elif formatfile == "json":
            json_file = json.dump(car_europe_list, cars_file, indent=4)

with open(f"filejapan.{formatfile}", "w", encoding="utf-8") as cars_file:
    for car in car_japan_list:
        car_japan = tuple(car)
        if formatfile == "txt":
            car = " ".join(car) + "\n"
            cars_file.write(car)

        elif formatfile == "csv":
            csv_file = csv.writer(cars_file, dialect="excel")
            csv_file.writerow(car_japan)

        elif formatfile == "json":
            json_file = json.dump(car_japan_list, cars_file, indent=4)

# vladalh@mail.ru

