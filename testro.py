import pandas as pd
import matplotlib.pyplot as plt


# 2 to 3120 amzn  == 3119
# 3121 to 6239 fb  == 3119
# 6240 to 9359 tsla  == 3119
# 9360 to 12477 google  == 3119
# 12478 to 15596 aapl  == 3119

df = pd.read_csv('stock_market_data.csv')
# print(df["Date"])
# print(type(df["Date"]))
# if "2019-08-31" in df["Date"].unique():
#     print("good")

