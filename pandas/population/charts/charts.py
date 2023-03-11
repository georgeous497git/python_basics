import matplotlib.pyplot as plt


def generate_bar_chart(labels, values, fig_name):
    # figure, coordinates
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.savefig(f'./chart_imgs/{fig_name}_bar_chart.jpg')
    plt.close()


def generate_pie_chart(labels, values, fig_name):
    # figure, coordinates
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    # plt.show()
    plt.savefig(f'./chart_imgs/{fig_name}_pie_chart.jpg')
    plt.close()
