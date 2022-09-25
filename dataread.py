import pandas as pd
from matplotlib import pyplot as plt
from FirstPeakDetection import FirstPeakDetection


def main():
    data = pd.read_excel("T File 5.xlsx", header=None, index_col=None)

    row, col = data.shape
    dev_x = range(0, col)

    standarddeviation = 5
    lag = 5
    peakdetection = FirstPeakDetection(data, lag, standarddeviation)
    peak = peakdetection.peakCalculation()
    for i in range(0, 2):
        dev_y = data.iloc[i, :]
        plt.scatter(dev_x, dev_y, marker='x', color='green')
        plt.scatter(peak[1], peak[0], marker='x', color='red')
        plt.show()


if __name__ == '__main__':
    main()


