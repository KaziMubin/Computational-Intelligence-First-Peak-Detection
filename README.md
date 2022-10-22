# Detecting first peak of a signal using automated robust and intelligent system

#### Abstruct
As part of Computational Intelligence course we did this project. We tried two different approach. 
  - Firstly, we tried to create one robust and automated solution. But making a solution which can detect first peak for all type of signal is quite hard. So we work
on only given signals.
- Secondly, we tried a ML approach using 'scikit-learn' library of python.

#### Generic signal processing
Signals are given in a .xlsx format. We used pandas `dataframe.readExel` to read the signal file. At frist we have to look at the signal file so there is no corrupted
data is given. As our second file had one or some string value we used  `conv.py` to manually convert all data to `float64`. As the signals were noisy we had to filter 
the signal. To do that we used highpass filter. It can also be done by applying window and convulation function. Then each signal is sent to the `scipy.signal.findpeaks` 
function. It detects **all the peaks**. But we needed only first peak with a specific definition. To get our **first peak** according to given definition we applied 
couple of filtering. First we added parameter **`distance=1000`**. Than we calculated average of all the peaks and selected the peak that is larger than all the peaks 
before and also larger than next peak.

#### ML solution
Signal files we were provided were not labeled so at first we used general signal processing to get the peaks and labeled the signal file. We used basic `scikit-learn` 
module to predict the peak position. We used regression models for getting the result. Due to time constrains we only tested with `linearRegression`and `SVM` regression 
models. To get the desired settings for training the data we used `gridsearchCV`. Between this two regression we got lowest error with `SVM`

### Ploting and GUI

A basic `TKinter` gui was used to upload the signal file. We used matplotlib to plot the signals.
