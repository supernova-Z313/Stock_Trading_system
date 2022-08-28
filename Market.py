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

    def manager(self):
        while self._first_page_state != "3":
            os.system("clear")  # change to cls
            print("              HELLO !!\nWelcome to the stock financial market. \n\n"
                  "what do you want to do: (1)sign up     (2)login\n           or           (3)next day    (4)exit")
            self._first_page_state = int(input())
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self._first_page_state == 1:
                os.system("clear")  # change to cls
                name = input("Please enter your first and last name:\n")
                national_code = int(input("Please enter your National Code:\n"))
                birth_date = input("Please enter your date of birth as an example: (zzzz:xx:yy)\n")
                first_balance = float(input("Please enter how much money you want to add to your account in first:\n"))
                username = input("Please choose a Username: \n")
                while username in self.__username_p:
                    username = input("This Username was chosen by another user. Please choose another Username:\n")
                while username == "0":
                    username = input("This value cant be your Username please try again: \n")
                pass_w = input("Please choose a Password: \n")
                os.system("clear")  # change to cls
                self.__username_p[username] = pass_w
                self.__users[username] = User(name, national_code, birth_date, self, first_balance)
                print("Account was successfully create. \nfor work with your account please login.")
                time.sleep(1)  # change time
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif self._first_page_state == 2:
                os.system("clear")  # change to cls
                use = None
                pass_c = None
                while (use not in self.__username_p) or (use in self.__username_p and pass_c != self.__username_p[use]):
                    use = input("Please enter your Username: (or for sign up enter 0)\n")
                    if use == "0":
                        break
                    pass_c = input("Please enter your Password: \n")
                if use != "0":
                    self.__users[use].work_station()
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif self._first_page_state == 3:
                for ind, i in enumerate(self._date_index):
                    self._date_index[ind] = i + 1
                self._date[0] = self._data.iloc[self._date_index[0]]["Date"]
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            else:
                break
    # -------------------------------------------------------------------------

    @property
    def date_index(self):
        return self._date_index
    # -------------------------------------------------------------------------

    @property
    def date(self):
        return self._date
    # -------------------------------------------------------------------------

    @property
    def data(self):
        return self._data


# =================================================================

