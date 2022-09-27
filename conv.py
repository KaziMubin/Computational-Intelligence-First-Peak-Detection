import numpy as np
import pandas as pd


def main():

    #new_Signal = pd.DataFrame(data=d, dtype=float)
    data = pd.read_excel('Wand_000.xlsx', header=None, index_col=None)

    row, col = data.shape

    new_list = np.zeros((row, col))

    print(row)
    print(col)

    for r in range(row):
        for c in range(col):
            val = data.iloc[r, c]
            val = val.astype(float)
            new_list[r][c] = val

    new_dataframe = pd.DataFrame(new_list)

    new_dataframe.to_excel("Wand_000_changed.xlsx")


if __name__ == '__main__':
    main()