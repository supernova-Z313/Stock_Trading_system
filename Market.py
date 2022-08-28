import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import time
import os
# =================================================================


class Market:
    def __init__(self, data_file_name: str = "stock_market_data", start_day: str = "2010-01-11"):
        self._data = pd.read_csv(f"{data_file_name}.csv")
        print("Load Market CSV Data       *")
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if start_day in self._data["Date"].unique():
            self._date = [start_day]
            self._date_index = self._data.index[self._data['Date'] == self._date[0]].tolist()
            print("Date set                   *")
        else:
            while start_day not in self._data["Date"].unique():
                if start_day[-2::] == "31":
                    mid = int(start_day[5:7]) + 1
                    if mid < 10:
                        start_day = start_day[0:5] + "0" + str(mid) + "-01"
                    else:
                        start_day = start_day[0:5] + str(mid) + "-01"
                else:
                    en = int(start_day[-2::]) + 1
                    if en < 10:
                        start_day = start_day[0:-2] + "0" + str(en)
                    else:
                        start_day = start_day[0:-2] + str(en)
            self._date = [start_day]
            self._date_index = self._data.index[self._data['Date'] == self._date[0]].tolist()
            print(f"The date entered is on holiday.\n"
                  f"We will continue our activities on the {self._date[0]}.")
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.__users = {}
        self.__username_p = {}
        self._first_page_state = None
        print("Loading was successfully   *")
        time.sleep(2)
    # -------------------------------------------------------------------------

