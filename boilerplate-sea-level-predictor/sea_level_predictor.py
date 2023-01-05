import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    
    fig, ax = plt.subplots(1, figsize=(15, 8))

    plt.scatter(x = df["Year"], y=df["CSIRO Adjusted Sea Level"])



    # Create first line of best fit
    
    
    line = linregress(x = df["Year"], y=df["CSIRO Adjusted Sea Level"])
    
    x_predict =list(range(1880, 2051))
    
    y_predict = []
    
    for year in x_predict:
        y_predict.append(line.intercept + line.slope * year)
        
    plt.plot(x_predict, y_predict, 'r', label='fitted line', color="green")  
    


    # Create second line of best fit
    
    df2 = df.loc[df["Year"] >= 2000]
        
    line2 = linregress(x = df2["Year"], y=df2["CSIRO Adjusted Sea Level"])
    
    x2_predict =list(range(2000, 2051))
    
    y2_predict = []
    
    for year in x2_predict:
        y2_predict.append(line2.intercept + line2.slope * year)
        
    plt.plot(x2_predict, y2_predict, 'r', label='second fitted line') 

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()