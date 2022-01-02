from cars import file_write, file_processing, file_reader


def main():
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


if __name__ == '__main__':
    main()
