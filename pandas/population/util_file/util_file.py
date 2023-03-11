import csv
import pandas as pd

def get_csv_data_pandas(path):
    data_frame = pd.read_csv(path)
    data_frame = data_frame[data_frame['Continent'] == 'Europe']
    countries = data_frame['Country/Territory'].values
    percentages = data_frame['World Population Percentage'].values

    return countries, percentages

def get_csv_data(path):
    header = []
    data = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Get the first line of the file

        for row in reader:
            data.append(row)

    return header, data
