import pandas as pd
import matplotlib.pyplot as plt


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

    def create_single_chan_histogram(self, mydata_df):
        fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
        mydata_df[(mydata_df['chan'] == int(self.chan)) &
                           (mydata_df['flags'] == self.flags) &
                           (mydata_df['pulse_height'] > self.min_pulse_height) &
                           (mydata_df['pulse_height'] < self.max_pulse_height)].hist(column='pulse_height', bins=self.bins, ax=axes)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

        return 0
