import charts.charts as charts
import util_file.util_file as file
import re


def get_data_chart(path, country):
    header, data = file.get_csv_data(path)
    go_on = True
    find_population = False

    labels_chart = []
    values_chart = []

    for row in data:
        # Generate tuples key: header, value: row
        iterable = zip(header, row)

        if go_on:
            for key, value in iterable:
                if 'Country' in key and country in value:
                    print('Country found:', value)
                    find_population = True
                    go_on = False

                if find_population and re.search('[0-9] Population', key):
                    print(f'Record: {key} - {value}')
                    labels_chart.append(key)
                    values_chart.append(int(value))
        else:
            break

    return labels_chart, values_chart


def generate_charts(labels, values):

    if len(labels) > 0 and len(values) > 0:
        charts.generate_pie_chart(labels, values)
        charts.generate_chart(labels, values)
    else:
        print('There is not data to generate charts')


if __name__ == '__main__':
    print("Challenge to generate 'matplotlib' charts reading data from a CSV file")
    input_country = 'Mexico'
    labels, values = get_data_chart('data/world_population.csv', input_country)
    generate_charts(labels, values)

