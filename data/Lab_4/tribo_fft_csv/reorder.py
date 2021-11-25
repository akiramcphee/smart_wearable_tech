# sort the data into chronological order inplace

import pandas as pd

filename = "Control 02 - 90 BPM" 
filename += "_filtered_fft.csv"
df = pd.read_csv(filename)
df = df[::-1]

savepath = "./chronological/" + filename
df.to_csv(savepath, index=False)