import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [15, 250, 303]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('bye.png')
    plt.close();