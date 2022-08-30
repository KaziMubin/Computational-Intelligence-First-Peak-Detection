import numpy as np


class FirstPeakDetection:

    def __init__(self, signal, lag, standarddeviation):
        self.data = []
        self.signal = signal
        self.row, self.col = signal.shape
        self.lag = lag
        self.firstpeak = np.zeros((self.row, 2))
        self.standarddeviation = standarddeviation
        self.deviation = np.zeros((self.row, self.col))
        self.mean = np.zeros((self.row, self.col))

    def peakCalculation(self):
        rowindex = 0

        for i in range(self.row):
            if i > 0:
                for j in range(1, self.col-1):
                    with_previous_index_value_difference = self.signal.iloc[i-1, j] - self.signal.iloc[i-1, j-1]
                    with_later_index_value_difference = self.signal.iloc[i-1, j] - self.signal.iloc[i-1, j+1]
                    with_previous_index_value_difference_percent = 100 * \
                                                                   (with_previous_index_value_difference / self.signal.iloc[i-1, j])
                    if (with_previous_index_value_difference > 0) & \
                            (with_later_index_value_difference > 0) & \
                            (with_previous_index_value_difference_percent > self.standarddeviation):
                        print('inside return##########################################')
                        print('#######################before assign{}##################'.format(self.firstpeak))
                        self.firstpeak[i-1][0] = self.signal.iloc[i-1, j]
                        self.firstpeak[i-1][1] = j
                        print('###############after assign{}################'.format(self.firstpeak))
                        return self.firstpeak
                    else:
                        continue

            self.mean[i][rowindex] = np.mean(self.signal.iloc[i, 0:(rowindex+self.lag)])
            print('#################'+str(self.mean[i][rowindex]))

            for x in range(rowindex):
                if self.signal.iloc[i, x] > self.mean[i][rowindex]:
                    signal_mean_difference = self.signal.iloc[i, x]-self.mean[i][rowindex]
                    signal_mean_difference_percentage = 100 * (float(signal_mean_difference)/float(self.signal.iloc[i, x]))
                    print('signal_mean_difference = '+str(signal_mean_difference))
                    print('##########')
                    print(self.signal.iloc[i, x])
                    print('##########')
                    print(self.mean[i][rowindex])
                    if signal_mean_difference_percentage > self.standarddeviation:
                        self.deviation[i][x] = signal_mean_difference_percentage
                    else:
                        continue
                else:
                    continue
            rowindex += 1

        print(str(self.row) + "###" + str(self.col))
