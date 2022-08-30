import pandas as pd
from matplotlib import pyplot as plt
from FirstPeakDetection import FirstPeakDetection


def main():
    data = pd.read_excel("T File 5.xlsx", header=None, index_col=None, usecols="G:DZZ")

    row, col = data.shape
    dev_x = range(0, col)

    standarddeviation = 5
    lag = 10
    peakdetection = FirstPeakDetection(data, lag, standarddeviation)
    peak = peakdetection.peakCalculation()
    for i in range(0, 2):
        dev_y = data.iloc[i, :]
        plt.plot(dev_x, dev_y, marker='x', color='green', linewidth='3')
        plt.plot(peak[1], peak[0], marker='x', color='red', linewidth='3')
        plt.show()


if __name__ == '__main__':
    main()


