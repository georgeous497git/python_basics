import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Get the first line of the file
        data = []

        for row in reader:
            # Generate tuples key: header, value: row
            iterable = zip(header, row)
            dictionary = {key: value for key, value in iterable}
            data.append(dictionary)
        return data


if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    print(data)
