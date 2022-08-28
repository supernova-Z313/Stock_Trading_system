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

# ind = df.index[df['Date'] == "2010-01-04"].tolist()
# print(df.iloc[5]["Date"])
compony = ["AMZN", "FB", "TSLA", "GOOGL", "AAPL"]
print(compony.index("FB"))
# print(df.to_string())
# x = 0
# print(df.iloc[5])
# print(df.iloc[3124])
# print(df.iloc[6243])
# print(df.iloc[9362])
# print(df.iloc[12481])


# for i in df["Date"]:
#     print(i)
#     if x == 10:
#         break
#     x += 1


# pd.options.display.max_rows = 200
# print(pd.options.display.max_rows)
# df.plot()
#
# plt.show()
