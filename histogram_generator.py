import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt, ceil


class hist_gen:
    def __init__(self, chan, max_pulse_height, min_pulse_height, bin_number, title, xlabel, ylabel):
        self.chan = chan
        self.flags = 1
        self.min_pulse_height = min_pulse_height
        self.max_pulse_height = max_pulse_height
        self.bins = bin_number
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def find_unique_channels(self, mydata_df):
        # This ended up being useless... oh well..
        col = 0
        row = 0
        self.channels_in_data = mydata_df.chan.unique()
        sqrt_num = sqrt(self.channels_in_data.size)

        if round(sqrt_num) > sqrt_num:
            row = round(sqrt_num)
            col = row
        elif round(sqrt_num) < sqrt_num:
            row = round(sqrt_num)
            col = ceil(sqrt_num)
        else:
            row = int(sqrt_num)
            col = row
        self.grid_rows = row
        self.grid_columns = col
        return 0

    def create_multi_chan_histogram(self, mydata_df):
        self.fig, self.axes = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k') # nrows=self.grid_rows, ncols=self.grid_columns,

        mydata_df[(mydata_df['flags'] == self.flags) &
                  (mydata_df['pulse_height'] > self.min_pulse_height) &
                  (mydata_df['pulse_height'] < self.max_pulse_height)].hist(column='pulse_height', bins=self.bins, by='chan', sharey=True, ax=self.axes)
        #plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        return 0

    def create_single_chan_histogram(self, mydata_df):
        self.fig, self.axes = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k') #sharex=True, sharey=True, nrows=1, ncols=1)
        mydata_df[(mydata_df['chan'].isin(self.chan)) &
                  (mydata_df['flags'] == self.flags) &
                  (mydata_df['pulse_height'] > self.min_pulse_height) &
                  (mydata_df['pulse_height'] < self.max_pulse_height)].hist(column='pulse_height', by='chan', figsize=(20, 20), bins=self.bins, ax=self.axes)
        plt.title(self.title + ' chan: ' + str(self.chan[0]))
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        return 0
