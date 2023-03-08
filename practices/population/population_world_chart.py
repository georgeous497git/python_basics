import util_file as file
import charts.charts as charts


def get_data_chart(path, columns):
    header, data = file.get_csv_data(path)

    labels_chart = []
    values_chart = []

    for row in data:
        # Generate tuples key: header, value: row
        iterable = zip(header, row)

        for key, value in iterable:
            if key.lower() in columns.get('key', 'none').lower():
                labels_chart.append(value)
                print(f'Country: {value}')

            if key.lower() in columns.get('value', 'none').lower():
                values_chart.append(float(value))
                print(f'Percentage: {value}')

    return labels_chart, values_chart


def generate_charts(c_labels, c_values):
    if len(c_labels) > 0 and len(c_values) > 0:
        charts.generate_pie_chart(c_labels, c_values)
        charts.generate_bar_chart(c_labels, c_values)
    else:
        print('There is not data to generate charts')


if __name__ == '__main__':
    print("Challenge to generate 'matplotlib' charts reading data from a CSV file for specific columns key-value")
    dictionary_columns = {'key': 'Country/Territory', 'value': 'World Population Percentage'}
    labels, values = get_data_chart('data/world_population.csv', dictionary_columns)
    generate_charts(labels, values)
