from scipy.signal import find_peaks
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
import pandas as pd
from tkinter import filedialog


def main():
    my_w = tk.Tk()
    my_w.geometry("400x300")  # Size of the window
    my_w.title('File Upload View')
    my_font1 = ('times', 18, 'bold')
    l1 = tk.Label(my_w, text='Upload File & read', width=30, font=my_font1)
    l1.grid(row=1, column=1)
    b1 = tk.Button(my_w, text='Upload File', width=20, command=lambda: upload_file())
    b1.grid(row=2, column=1)
    my_w.mainloop()


def upload_file():
    file = filedialog.askopenfilename()

    data = pd.read_excel(file, header=None, index_col=None)
    row, col = data.shape
    dev_x = range(0, col)

    for i in range(1, 3):
        first_peak = np.zeros(1)
        location = np.zeros(1)
        peaks = []
        dev_y = data.iloc[i, :]
        indexes, _ = find_peaks(dev_y, distance=1000)
        for vals in range(len(indexes)):
            peaks.append(dev_y[indexes[vals]])
            print(peaks)

        mean_indexes = np.average(peaks)
        print(mean_indexes)

        for i in range(0, len(indexes) - 1):
            if (i == 0) & (dev_y[indexes[i]] > dev_y[indexes[i + 1]]):
                first_peak = dev_y[indexes[i]]
                location = indexes[i]
            elif (i > 0) & (dev_y[indexes[i]] > mean_indexes) & \
                    (dev_y[indexes[i]] > dev_y[indexes[i + 1]]) & (dev_y[indexes[i]] > dev_y[indexes[i - 1]]):
                first_peak = dev_y[indexes[i]]
                location = indexes[i]
        print(first_peak)
        print(location)

        plt.plot(dev_x, dev_y, color='green')
        plt.plot(location, first_peak, marker='x', color='red')
        plt.show()


if __name__ == '__main__':
    main()

