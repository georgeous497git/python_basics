import csv


def get_csv_data(path):
    header = []
    data = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Get the first line of the file

        for row in reader:
            data.append(row)

    return header, data
