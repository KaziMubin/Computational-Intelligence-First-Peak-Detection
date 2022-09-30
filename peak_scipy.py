import numpy as np
from scipy.signal import find_peaks, butter, filtfilt
from matplotlib import pyplot as plt
import tkinter as tk
import pandas as pd
from tkinter import filedialog
import ML_approch


def main():
    my_w = tk.Tk()
    my_w.geometry("400x300")  # Size of the window
    my_w.title('File Upload View')
    my_font1 = ('times', 18, 'bold')
    l1 = tk.Label(my_w, text='Upload File & read', width=30, font=my_font1)
    l1.grid(row=1, column=1)
    b1 = tk.Button(my_w, text='Upload File', width=20, command=lambda: upload_file())
    b2 = tk.Button(my_w, text='ML Solution', width=20, command=lambda: ML_sol())
    b1.grid(row=2, column=1)
    b2.grid(row=3, column=1)

    my_w.mainloop()


def ML_sol():
    ML_approch.ML_solution()

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

        b, a = butter(3, 0.1, 'highpass')
        filtered2 = filtfilt(b, a, dev_y)
        filtered3 = filtfilt(b, a, filtered2)

        indexes, _ = find_peaks(filtered3, distance=1000)
        for vals in range(len(indexes)):
            peaks.append(filtered3[indexes[vals]])
            print(peaks)

        mean_indexes = np.average(peaks)
        print(mean_indexes)

        for ind in range(0, len(indexes)-1):
            if (ind == 0) & (filtered3[indexes[ind]] > filtered3[indexes[ind+1]]):
                first_peak = filtered3[indexes[ind]]
                location = indexes[ind]
            elif (ind > 0) & (filtered3[indexes[ind]] > mean_indexes) & \
                    (filtered3[indexes[ind]] > filtered3[indexes[ind+1]]) &\
                    (filtered3[indexes[ind]] > filtered3[indexes[ind-1]]):
                first_peak = filtered3[indexes[ind]]
                location = indexes[ind]
        print(first_peak)
        print(location)
        #first_peak = dev_y[indexes[0]]
        #location = indexes[0]
        plt.figure()
        plt.plot(filtered3, color='green')
        plt.plot(location, first_peak, marker='x', color='red')
        plt.show()


if __name__ == '__main__':
    main()

