# Using python libraries
> Use matplotlib and pandas to handle and plot data from iris.data,
and use numpy to create random MxN csv file.

In this project we develop tools to create a csv file from random numbers on
the interval [0,1) with any shape (rows, columns). We also create a script to
plot various characteristics of an iris flow using data from iris.data.

## Installation

With Anaconda, simply run: 

```sh
conda install assignment-7-using-libraries-doqhne
```

## Usage example

To create plots from iris.data, simply run:

```sh
$ python plotter.py
```

Three plots will be saved to the current directory:
1. A boxplot of the values in each column (sepal_length, 
    sepal_width, petal_length, petal_width)
2. A scatter plot of the sepal_lengths vs widths, with color coding for
    each of the three species in the dataset
3. A panel plot with the above 2 plots side by side in one figure
    
To create a csv file populated with random numbers between 0 and 1:
1. Import data_processor.py
2. Create the csv file with:
    data_processor.write_matrix_to_file(num_rows, num_columns, 'myfile.csv') 

## Release History

* v1.0
    * Initial version that creates the three plots described above, and a
        function to create a random MxN csv file.
