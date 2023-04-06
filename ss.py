# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os

ticker='GS'
input_dir = r'/Users/shubhgoyal/Desktop/Data Sci/week_1_homework'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    def analyze_returns(lines):
        lines = lines[1:]
        dict_return = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
        dict_mean = {}
        dict_sd = {}
        dict_R_minus = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
        dict_R_plus = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }

        # read data line by line and store in dict
        for line in lines:
            data = line.split(',')
            day = data[4]
            close = float(data[10])
            ret = float(data[13])

            # analyze the daily returns for each day of the week
            if day in dict_return:
                dict_return[day].append(ret)

                if ret >= 0:
                    dict_R_plus[day].append(ret)
                else:
                    dict_R_minus[day].append(ret)

                if day not in dict_mean:
                    dict_mean[day] = 0
                    dict_sd[day] = 0

                dict_mean[day] += (close != 0) * ((close - float(data[7])) / close) * 100
                dict_sd[day] += ((close != 0) * ((close - float(data[7])) / close) * 100 - dict_mean[day]) ** 2

        for key in dict_mean:
            dict_mean[key] /= len(dict_return[key])
            dict_sd[key] = (dict_sd[key] / len(dict_return[key])) ** 0.5

        dict_mean_R_minus = {k: round(sum(v) / len(v), 3) for k, v in dict_R_minus.items()}
        dict_mean_R_plus = {k: round(sum(v) / len(v), 3) for k, v in dict_R_plus.items()}
        dict_sd_R_minus = {k: round((sum([(x - dict_mean_R_minus[k]) ** 2 for x in v]) / len(v)) ** 0.5, 3) for k, v in dict_R_minus.items()}
        dict_sd_R_plus = {k: round((sum([(x - dict_mean_R_plus[k]) ** 2 for x in v]) / len(v)) ** 0.5, 3) for k, v in dict_R_plus.items()}

        print('Mean daily return for each day of the week:', dict_mean)
        print('Standard deviation of daily return for each day of the week:', dict_sd)
        print('Mean R-:', dict_mean_R_minus)
        print('Mean R+:', dict_mean_R_plus)
        print('SD R-:', dict_sd_R_minus)
        print('SD R+:', dict_sd_R_plus)

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)



    analyze_returns(lines)









