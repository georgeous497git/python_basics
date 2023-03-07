import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    # figure, coordinates
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    # figure, coordinates
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['Casper', 'Maylo', 'Spike']
    values = [6, 2, 1.5]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
