import matplotlib.pyplot as plt


def generate_chart(labels, values):
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