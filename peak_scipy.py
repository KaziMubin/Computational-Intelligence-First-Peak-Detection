from scipy.signal import find_peaks
from matplotlib import pyplot as plt
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
    dev_x = range(col)
    dev_y = data.iloc[35, :]
    indexes, _ = find_peaks(dev_y, distance=1000)

    first_peak = dev_y[indexes[0]]
    location = indexes[0]
    plt.plot(dev_x, dev_y, color='green')
    plt.plot(location, first_peak, marker='x', color='red')
    plt.show()


if __name__ == '__main__':
    main()

