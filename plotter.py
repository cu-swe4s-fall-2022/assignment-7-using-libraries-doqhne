import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in data
iris = pd.read_csv('iris.data')

# Name columns
iris.columns = ['sepal_width',
                'sepal_length',
                'petal_width',
                'petal_length',
                'species']

# Create the boxplot
measurement_names = ['sepal_length',
                     'sepal_width',
                     'petal_width',
                     'petal_length']
fig = plt.figure()
plt.boxplot(iris[measurement_names], labels=measurement_names)
plt.ylabel('cm')
fig.savefig('boxplot.png')
plt.show()

# Create the scatter plot
fig = plt.figure()
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['sepal_length'],
                iris_subset['sepal_width'],
                label=species_name,
                s=5)
    plt.legend(loc='upper right')
    plt.xlabel('sepal_length (cm)')
    plt.ylabel('sepal_width (cm)')
plt.show()
fig.savefig('petal_width_v_length_scatter.png')

# Create the panel plot

fig, axes = plt.subplots(1, 2)
fig.set_size_inches(15, 6)

# left plot
axes[0].boxplot(iris[measurement_names], labels=measurement_names)
axes[0].set_ylabel('cm')

# right scatter plot
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['sepal_length'],
                    iris_subset['sepal_width'],
                    label=species_name,
                    s=5)
    axes[1].legend(loc='upper right')
    axes[1].set_xlabel('sepal_length (cm)')
    axes[1].set_ylabel('sepal_width (cm)')

# loop through each column
for j in range(2):
    # choose to hide of show certain borders or "spines"
    axes[j].spines['top'].set_visible(False)
    axes[j].spines['right'].set_visible(False)
plt.savefig('multi_panel_figure.png')
plt.show()
