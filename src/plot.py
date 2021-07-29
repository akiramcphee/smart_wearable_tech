import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# # Set up plot specifications
# sns.set(style='ticks')
# sns.axes_style('white')
# sns.set_context('paper')
# plt.rcParams['figure.figsize'] = [10, 5]
# plt.rcParams.update({'font.size': 12})
# rcParams['font.family'] = 'Avenir'


def csv_format(word: str, lab_num: str, index: str, speaker: str, sensor_ch: int):
    '''
        Format oscilloscope files for easier manipulation and plotting
        Inputs:
            lab_num (int)       Lab number of the scope to be formatted
            scope_num (int)     scope number of the file to be formatted
        Outputs:
            save_path (str)     path to the formatted file from the root directory
    '''

    # NEW FORMAT
    filename = f'{word}_{lab_num}_{index}_{speaker}'
    df = pd.read_csv(f'../data/{word}/Raw/{filename}.csv')

    # Rename columns
    cols = list(df.columns)
    for header in cols:
        if 'axis' in header:
            df.rename({header: 'Time'}, axis=1, inplace=True)
        elif str(sensor_ch) in header:
            df.rename({header: 'Sensor'}, axis=1, inplace=True)
        else:
            df = df.drop(columns=[header])

    # Delete row with units (first row)
    df = df.drop(0)

    # Delete completley empty rows, and remove indexes from the csv
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)

    # Convert from scientific to float
    cols = list(df.columns)
    for header in cols:
        df[header].apply(lambda x: '%.7f' % x)

    # Correct any negative timestamps
    t0 = df['Time'][0]
    if t0 < 0:
        df['Time'] = df['Time'].astype(float) - t0

    # Save modified csv to a new file, display first 10 rows
    #save_path = f'../data/Lab_{lab_num}/Formatted/scope_{scope_num}.csv'
    # NEW FORMAT
    save_path = f'data/{word}/Formatted/{filename}.csv'

    df.to_csv(save_path, index=False)

    return str(save_path)


def linear_plot(word: str, lab_num: str, index: str, speaker: str, sensor_ch: int):
    formatted_filename = f'{word}_{lab_num}_{index}_{speaker}'

    filename = csv_format(word, lab_num, index, sensor_ch, speaker)
    df = pd.read_csv(filename, delimiter=',', skiprows=0)

    # initialise data for anaysis
    dt = 1
    t = df['Time']
    f = df['Sensor']

    # Plot Raw data from CSV
    plt.plot(t, f, LineWidth=1, label="scope_0 raw", color='#001E92')
    plt.xlabel('Time (s)')
    plt.ylabel('Volatage (V)')
    plt.title(f'Raw data from {filename}')
    plt.legend()

    # save raw scope as png in data/plots
    image_path = f'../data/Plots/{word}/Line_plots/{formatted_filename}.png'
    plt.savefig(image_path, dpi=300, bbox_inches='tight', transparent=False)

    plt.show()
    pass
