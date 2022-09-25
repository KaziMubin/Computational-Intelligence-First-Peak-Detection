import numpy as np


class FirstPeakDetection:

    def __init__(self, signal, lag, standarddeviation):
        self.data = []
        self.signal = signal
        self.row, self.col = signal.shape
        self.lag = lag
        self.firstpeak = np.zeros((self.row, 2))
        self.standarddeviation = standarddeviation
        self.greater_than_mean = np.zeros((self.row, self.col))
        self.mean = np.zeros((self.row, self.col))
        self.peaks = np.zeros((self.row, self.col))

    def peakCalculation(self):
        # col = 0
        number_of_point_over_mean = 0


        for i in range(self.row):

            mean_total = np.mean(self.signal.iloc[i, 0:self.col])
            for col in range(self.col):
                self.mean[i][col] = np.mean(self.signal.iloc[i, (col - self.lag):(col + self.lag)])
                print('############################################' + str(self.mean[i][col]))

                if (self.signal.iloc[i, col] > self.mean[i][col]) & (self.signal.iloc[i, col] != 0):
                    signal_mean_difference = self.signal.iloc[i, col] - self.mean[i][col]
                    signal_mean_difference_percentage = 100 * (
                            float(signal_mean_difference) / float(self.signal.iloc[i, col]))

                    print('####################################### signal value')
                    print(self.signal.iloc[i, col])
                    print('###################################### mean at this point')
                    print(self.mean[i][col])

                    if signal_mean_difference_percentage > self.lag:
                        self.greater_than_mean[i][col] = self.signal.iloc[i, col]

                else:
                    continue

            for v in range(self.col):
                if self.signal.iloc[i, v] > mean_total:
                    number_of_point_over_mean += 1

            number_of_point_over_mean_percent = 100 * (number_of_point_over_mean / self.col)

            if number_of_point_over_mean_percent > 20:
                first_peak = self.continuous_peak(mean_total)
                return first_peak
            else:
                first_peak = self.discrete_peak(mean_total)
                return first_peak

        print(str(self.row) + "###" + str(self.col))

    def continuous_peak(self, mean):
        peaks_value = np.zeros(self.col)
        first_peak = np.zeros(2)
        for row in range(self.row):
            p = 0
            for col in range(1,self.col-1):
                if (self.greater_than_mean[row][col] > mean) & \
                        (self.greater_than_mean[row][col] > self.greater_than_mean[row][col-1]) & \
                        (self.greater_than_mean[row][col] > self.greater_than_mean[row][col+1]):

                    self.peaks[row][col] = self.signal.iloc[row, col]
                    peaks_value[p] = self.signal.iloc[row, col]
                    p += 1
                else:
                    continue
            i=1
            while 1:
                if (peaks_value[i]> peaks_value[i+1]) & (peaks_value[i]> peaks_value[i-11]) & (i < self.col):
                    for col in range(self.col):
                        if self.signal.iloc[row, col] == peaks_value[i]:
                            first_peak[0] = self.signal.iloc[row, col]
                            first_peak[1] = col

                    return first_peak
                else:
                    i += 1

    def discrete_peak(self, mean):
        first_peak = np.zeros(2)
        for row in range(self.row):

            for col in range(self.col):
                if self.greater_than_mean[row][col] > mean:
                    first_peak[0] = self.signal.iloc[row, col]
                    first_peak[1] = col
                else:
                    continue

        return first_peak
























# if i > 0:
#     for j in range(1, self.col - 1):
#         with_previous_cell_value_difference = self.signal.iloc[i - 1, j] - self.signal.iloc[i - 1, j - 1]
#         with_later_cell_value_difference = self.signal.iloc[i - 1, j] - self.signal.iloc[i - 1, j + 1]
#         with_previous_cell_value_difference_percent = 100 * \
#                                                       (with_previous_cell_value_difference / self.signal.iloc[i - 1, j])
#         if (with_previous_cell_value_difference > 0) & \
#                 (with_later_cell_value_difference > 0) & \
#                 (with_previous_cell_value_difference_percent > self.standarddeviation):
#             print('inside return##########################################')
#             print('#######################before assign{}##################'.format(self.firstpeak))
#             self.firstpeak[i - 1][0] = self.signal.iloc[i - 1, j]
#             self.firstpeak[i - 1][1] = j
#             print('###############after assign{}################'.format(self.firstpeak))
#             return self.firstpeak
#         else:
#             continue




# self.greater_than_mean[i][col] = signal_mean_difference_percentage
                    # if signal_mean_difference_percentage > self.standarddeviation:
                    #
                    #     self.greater_than_mean[i][col] = signal_mean_difference_percentage
                    # else:
                    #     continue