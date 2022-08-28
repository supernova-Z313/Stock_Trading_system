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
class User:
    def __init__(self, name, code, birth, parent: Market, balance: float = 0):
        self.name = name
        self.code = code
        self.birth = birth
        self.balance = balance
        self.data = parent.data
        self.date = parent.date
        self.date_index = parent.date_index
        self.currency_balance = {}
    # -------------------------------------------------------------------------

    def work_station(self):
        command = None
        while command != 7:
            os.system("clear")  # change to cls
            print(f"Welcome to the home page                   Date:{self.date[0]}\n")
            print("What do you want to do? \n"
                  " + Buy a currency                                  (0)\n"
                  " + Sell a currency                                 (1)\n"
                  " + Deposit to account                              (2)\n"
                  " + See market price changes                        (3)\n"
                  " + View assets and account balances                (4)\n"
                  " + View chart of price changes                     (5)\n"
                  " + Linear regression chart of price changes        (6)\n"
                  " + Exit from your profile                          (7)")
            command = int(input())
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if command == 0:
                day_data = {"0": ["Symbol",	"Open",	"Volume"]}
                for ind, i in enumerate(self.date_index, start=1):
                    i = self.data.iloc[i]
                    day_data[f"{ind}"] = [i["Symbol"], i["Open"], i["Volume"]]
                com = None

                while com != 0:
                    os.system("clear")  # change to cls
                    print(f"Market state:                                         Date:{self.date[0]}")
                    print(pd.DataFrame(day_data), end="\n\n")
                    print(f"Your Balance account:                                             {self.balance}")
                    com = int(input("To buy any currency, enter its number in the list or enter 0 to exit:\n"))
                    if com == 1:
                        amount = float(input("amount of this currency:   "))
                        while (amount * float(day_data["1"][1]) > self.balance) or (amount * float(day_data["1"][1]) > float(day_data["1"][2])):
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        if day_data["1"][0] in self.currency_balance:
                            self.currency_balance[day_data["1"][0]] += amount
                        else:
                            self.currency_balance[day_data["1"][0]] = amount
                        self.balance -= amount * float(day_data["1"][1])
                        print("The purchase was successful.")
                        time.sleep(1.5)
                    elif com == 2:
                        amount = float(input("amount of this currency:   "))
                        while (amount * float(day_data["2"][1]) > self.balance) or (amount * float(day_data["2"][1]) > float(day_data["2"][2])):
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        if day_data["2"][0] in self.currency_balance:
                            self.currency_balance[day_data["2"][0]] += amount
                        else:
                            self.currency_balance[day_data["2"][0]] = amount
                        self.balance -= amount * float(day_data["2"][1])
                        print("The purchase was successful.")
                        time.sleep(1.5)
                    elif com == 3:
                        amount = float(input("amount of this currency:   "))
                        while (amount * float(day_data["3"][1]) > self.balance) or (amount * float(day_data["3"][1]) > float(day_data["3"][2])):
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        if day_data["3"][0] in self.currency_balance:
                            self.currency_balance[day_data["3"][0]] += amount
                        else:
                            self.currency_balance[day_data["3"][0]] = amount
                        self.balance -= amount * float(day_data["3"][1])
                        print("The purchase was successful.")
                        time.sleep(1.5)
                    elif com == 4:
                        amount = float(input("amount of this currency:   "))
                        while (amount * float(day_data["4"][1]) > self.balance) or (amount * float(day_data["4"][1]) > float(day_data["4"][2])):
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        if day_data["4"][0] in self.currency_balance:
                            self.currency_balance[day_data["4"][0]] += amount
                        else:
                            self.currency_balance[day_data["4"][0]] = amount
                        self.balance -= amount * float(day_data["4"][1])
                        print("The purchase was successful.")
                        time.sleep(1.5)
                    elif com == 5:
                        amount = float(input("amount of this currency:   "))
                        while (amount * float(day_data["5"][1]) > self.balance) or (amount * float(day_data["5"][1]) > float(day_data["5"][2])):
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        if day_data["5"][0] in self.currency_balance:
                            self.currency_balance[day_data["5"][0]] += amount
                        else:
                            self.currency_balance[day_data["5"][0]] = amount
                        self.balance -= amount * float(day_data["5"][1])
                        print("The purchase was successful.")
                        time.sleep(1.5)

            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif command == 1:
                day_data = {"0": ["Symbol",	"Open",	"Volume"]}
                for ind, i in enumerate(self.date_index, start=1):
                    i = self.data.iloc[i]
                    day_data[f"{ind}"] = [i["Symbol"], i["Open"], i["Volume"]]
                com = None

                if len(self.currency_balance) == 0:
                    os.system("clear")  # change to cls
                    input("You have no currency to sell, please buy some first.")
                    com = 0
                while com != 0:
                    currency_data_frame = {0: ["Symbol", "Amount", "Volume"]}
                    z_a = []
                    for ind, i in enumerate(self.currency_balance, start=1):
                        adel = None
                        for j in self.date_index:
                            j = self.data.iloc[j]
                            if j["Symbol"] == i:
                                adel = j["Open"]
                                z_a.append(adel)
                                break
                        currency_data_frame[ind] = [i, self.currency_balance[i], self.currency_balance[i] * adel]
                    os.system("clear")  # change to cls
                    print(f"Market state:                                         Date:{self.date[0]}")
                    print(pd.DataFrame(day_data), end="\n\n")
                    print("Account state:    ")
                    print(pd.DataFrame(currency_data_frame), end="\n\n")
                    print(f"Your Balance account:                                        {self.balance}")
                    com = int(input("To sell any currency, enter its number in the list or enter 0 to exit:\n"))
                    if com == 1:
                        amount = float(input("amount of this currency:    "))
                        while amount > currency_data_frame[1][1]:
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        self.currency_balance[currency_data_frame[1][0]] -= amount
                        self.balance += z_a[0] * amount
                        print("Currency sold successfully.")
                        time.sleep(2)
                    elif com == 2:
                        amount = float(input("amount of this currency:    "))
                        while amount > currency_data_frame[2][1]:
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        self.currency_balance[currency_data_frame[2][0]] -= amount
                        self.balance += z_a[1] * amount
                        print("Currency sold successfully.")
                        time.sleep(2)
                    elif com == 3:
                        amount = float(input("amount of this currency:    "))
                        while amount > currency_data_frame[3][1]:
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        self.currency_balance[currency_data_frame[3][0]] -= amount
                        self.balance += z_a[2] * amount
                        print("Currency sold successfully.")
                        time.sleep(2)
                    elif com == 4:
                        amount = float(input("amount of this currency:    "))
                        while amount > currency_data_frame[4][1]:
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        self.currency_balance[currency_data_frame[4][0]] -= amount
                        self.balance += z_a[3] * amount
                        print("Currency sold successfully.")
                        time.sleep(2)
                    elif com == 5:
                        amount = float(input("amount of this currency:    "))
                        while amount > currency_data_frame[5][1]:
                            amount = float(input("Operation is not possible, please try again.\n"
                                                 "amount of this currency:    "))
                        self.currency_balance[currency_data_frame[5][0]] -= amount
                        self.balance += z_a[4] * amount
                        print("Currency sold successfully.")
                        time.sleep(2)
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
