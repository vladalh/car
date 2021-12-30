import csv
import json


def file_reader():
    gap_file = []
    with open(f"cars.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=";")
        header = next(csv_reader)
        for line in csv_reader:
            gap_file.append(line)
        return gap_file


def file_processing(gap_file, country):
    car_list = []
    for line in gap_file:
        if country in line:
            car_list.append(line)
            car_list.sort(key=lambda x: x[0])
    return car_list


def file_write(fileformat, country, car_list):
    with open(f"file{country}.{fileformat}", "w", encoding="utf-8") as file:
        for car in car_list:
            car_tuple = tuple(car)
            if fileformat == "txt":
                car = " ".join(car) + "\n"
                txt_file = file.write(car)
            elif formatfile == "csv":
                csv_file = csv.writer(file, dialect="excel")
                csv_file.writerow(car_tuple)
            elif formatfile == "json":
                json_file = json.dump(car_list, file, indent=4)


formatfile_list = ["txt", "csv", "json"]

country_list = ["US", "Europe", "Japan"]

formatfile = input("Enter the file format for saving data: txt, csv or json: ")

country = input("Enter the name of the car manufacturer: US, Europe or Japan ")

if formatfile not in formatfile_list:
    print("You entered the wrong file format")
    exit(0)

if country not in country_list:
    print("You entered the wrong country of origin")
    exit(0)


file_write(formatfile, country, file_processing(file_reader(), country))

# vladalh@mail.ru

