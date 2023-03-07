import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        total = 0

        for _, value in reader:
            total += int(value)
        return total


if __name__ == '__main__':
    print(read_csv('./data.csv'))

