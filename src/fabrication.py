import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.io.parsers import read_csv
import seaborn as sns
import random
from plot import csv_format
# Set up plot specifications
sns.set(style='ticks')
sns.axes_style('white')
sns.set_context('paper')
plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams.update({'font.size': 12})
rcParams['font.family'] = 'Avenir'


def generate_random_variation(filename, var_num, kind):
    '''
    Generates a completely random variation of the parent file

    Arguments:
        filename (str)          - The parent file name
        var_num (int)           - The variation number to be saved under. Default won't save anything
        kind (str)              - The format of the generated child. 


    Return Value:
        None

    '''

    # Decide how many times the data is going to be manipulated, random for greater variability
    df = pd.read_csv(filename)

    if kind == 'comparison_image':
        plt.plot(df['Time'], df['Sensor'])

    # Plot features
    plt.title("Comparison of randomly generated child to parent")
    plt.xlabel("Time (s)")
    plt.ylabel("Sensor")

    loop = random.randint(6, 20)
    i = 0
    while i < loop:
        # Decides which method of manipulation is going to be applied
        fabrication_type = random.randint(2, 3)

        # Mirror the data (Although probsably not useful)
        if fabrication_type == 1:
            df["Sensor"] = df["Sensor"].values[::-1]

        # Scale up by a random percentage
        elif fabrication_type == 2:
            scale(df)

        # Shift by random amount
        elif fabrication_type == 3:
            shift(df)

        i += 1
    # Clean off ends
    for k, v in df.iteritems():
        v[v < 0] = 0
        v[v > 5] = 5

    plt.plot(df['Time'], df['Sensor'])
    # if var_num == 0:
    # plt.show()
    # Save plot
    if (kind == 'image' or kind == 'comparison_image'):
        plt.clf()
        plt.specgram(df['Sensor'], Fs=2, cmap="rainbow", noverlap=250)
        plt.axis(False)
        scope_num = filename[:-4]
        scope_num = scope_num[-1]
        image_path = f'fabricated_data/{scope_num}/scope{scope_num}_var_{var_num}.png'
        plt.savefig(image_path, dpi=300,
                    bbox_inches='tight', transparent=False)
    elif kind == 'csv' and var_num > 0:
        df.to_csv(f'{filename}_var_{var_num}.csv', index=False)

    # Clear plot for the next variation, matplotlib doesn't do this automatically
    plt.clf()
    pass


def scale(df):
    '''
    Scales random items in the dataframe by a random amount 

    Arguments:
        df (dataframe)          - Read from the chosen file

    Return Value:
        None

    '''
    j = 0
    while j < len(df["Sensor"]):
        # Scale factor is not same each time
        scale_factor = random.randint(7, 14)/10
        # Determines the spacing between elements to get scaled
        scale_element = random.randint(4, 100)
        scale_neighbour = random.randint(2, 10)
        if j % scale_element == 0:
            df["Sensor"][j:scale_neighbour+j] *= (scale_factor)
        j += 1
    pass


def shift(df):
    '''
    Shifts random items in the dataframe (both horizontally and vertically) by a random amount 

    Arguments:
        df (dataframe)          - Read from the chosen file

    Return Value:
        None

    '''
    # Scale factor is not same each time
    shift_factor_x = random.randint(-50, 100)/100
    shift_factor_y = random.randint(-5, 10)/2000

    df["Time"] += (shift_factor_x)
    df["Sensor"] += (shift_factor_y)

    pass


if __name__ == '__main__':
    filename = 'fabricated_data/csv/scope_0.csv'
    generate_random_variation(filename, 0, 'image')
