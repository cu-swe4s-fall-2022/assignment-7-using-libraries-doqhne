#!/bin/bash

# test plotter.py - make sure files are outputted
python plotter.py

if [ -f "./boxplot.png" ];
then
    echo "File boxplot.png exists"
else 
    echo "File boxplot.png does not exist"
fi

if [ -f "./petal_width_v_length_scatter.png" ];
then
    echo "File petal_width_v_length_scatter.png exists"
else 
    echo "File petal_width_v_length_scatter.png does not exist"
fi

if [ -f "./multi_panel_figure.png" ];
then
    echo "File multi_panel_figure.png exists"
else 
    echo "File multi_panel_figure.png does not exist"
fi

rm *.png