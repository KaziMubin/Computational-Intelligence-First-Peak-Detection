import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV


def main():

    train = pd.read_excel("labeled.xlsx")
    test = pd.read_excel("Wand_000_changed.xlsx")

    y_train = train.Class  # if y is only one column
    train.drop(['Class'], axis=1, inplace=True)
    X_train = train

    y_test = test.Class
    test.drop(['Class'], axis=1, inplace=True)
    X_test= test

    # y = train.Class
    # train.drop(['Class'], axis=1, inplace=True)
    # X = train

    # Now we split the dataset in train and test part
    # here the train set is 75% and test set is 25%
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    DT = SVR()
    #print(DT.get_params())
    cross_val = GridSearchCV(estimator=DT,
                             param_grid={'max_iter':[-1, 100, 500, 750, 1000]},
                             cv=4)
    cross_val.fit(X_train, y_train)
    #DT.fit(X_train, y_train)
    pred = cross_val.predict(X_test)

    print("The first five prediction {}".format(pred[525:]))
    print("The real first five labels {}".format(y_test[525:]))

    #print(mean_absolute_error(y_test, pred))
    print(mean_absolute_error(y_test, pred))
    print("#####################################################")
    print(pd.DataFrame(cross_val.cv_results_))


if __name__ == "__main__":
    main()
