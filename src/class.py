
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot import csv_format, linear_plot


class Plot(object):

    def __init__(self, word):
        self.word = word

    def line_plot(self, lab_num, index, speaker, sensor_ch):
        self.lab_num = lab_num
        self.index = index
        self.speaker = speaker
        self.sensor_ch = sensor_ch

        # Formatting the file
        filename = f'../data/{self.word}/Formatted/{self.word}_{lab_num}_{index}_{speaker}.csv'
        csv_format(self.word, self.lab_num, self.index,
                   self.speaker, self.sensor_ch)

        linear_plot(self.word, self.lab_num, self.index,
                    self.speaker, self.sensor_ch)
        return True


alpha = Plot('alpha')
print(alpha.line_plot('00', '01', 'am', 2))
