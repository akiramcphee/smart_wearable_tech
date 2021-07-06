# Data 📊

This section describes how the team has organised our data and where to retrieve specific files and plots. 

## File Naming Convention

- Files will be named using the following convention:
```
  <word>_<lab_num>_<index>_<speaker>.csv

```
 - where `<word>` is the word spoken, `<lab_num>` is the lab where the data was acquired(full information about each lab can be found in the table at the bottom of the README.md), `<index>` tells which repetition of the word the data represents and `<speaker>` refers to who the test subject was
- An example would be `alpha_00_23_AM.csv`

## Audio 🔈

- This directory contains the .wav files generated from csv data acquired during Labs.

## Lab\_# ⚡

- This directory contains call data obtained and processed from the corresponding lab. It is divided into two sections, `Raw` and `Filtered`

  ### Raw

  - Raw data obtained from lab sessions in the form of a CSV file.

  ### Filtered

  - Filtered version of the raw csv files. Divided into two sections, `Bandpass` and `FFT`.

    #### Bandpass

    - Filtered data using the method of applying a Bandpass filter.
    - Source file: `bandpass.ipynb`

    #### FFT

    - Filtered data using the method of applying an FFT.
    - Source file: `fft.ipynb`

## Plots 📈

- This is where all the plots generated are stored.
- They are divided into Lab numbers and then into categories. The four categories currently in place are:

  1. `Bandpass_filtered_plots`
  2. `FFT_comparison_plots`
  3. `Line_plots`
  4. `Spectrograms`

  ### Bandpass_filtered_plots

  - Plot generated of data after a bandpass filter has been applied.
  - Source file: `bandpass.ipynb`

  ### FFT_comparison_plots

  - Plot generated of data after an FFT has been applied.
  - Source file: `fft.ipynb`

  ### Line_plots

  - Plot generated of raw data obtained from labs.
  - Source file: `fft.ipynb`

  ### Spectrograms

  - Spectrogram generated of raw data obtained from labs.
  - Source file: `spectrogram.ipynb`

# Lab File Table

- These are just temporary inclusions to the table, Lab 00 will actually be the next lab we have so we can propely acquire data in the format we settled on.
- Feel free to play around with the table to learn how html tables work. Also, add any new keys (`Subject`, `Date` etc) to the `notes` section if you think it's appropriate.

<table>
  <tr>
    <th>Lab Number</th>
    <th>Sensor Number</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><br>Lab 00<br /><br />
    <td><b>1,2,3</b>
    <td>
      <b>Subject:</b> Dave 
      <br><b>Date:</b> 03/21 
      <br><b>Words:</b> alpha,bravo,charlie,Zulu
    </td>

  </tr>
    <tr>
    <td><br>Lab 01<br /><br />
    <td><b>1,2,3</b>
    <td>
      <b>Subject:</b> Andrew
      <br><b>Date:</b> 03/27 
      <br><b>Words:</b> alpha,bravo,charlie,Zulu
    </td> 
  </tr>
    <tr>
    <td><br>Lab 02<br /><br />
    <td><b>1,2,3</b>
    <td>
      <b>Subject:</b> Akira
      <br><b>Date:</b> 06/25 
      <br><b>Words:</b> alpha,bravo,charlie,Zulu
    </td> 
  </tr>
  
</table>
