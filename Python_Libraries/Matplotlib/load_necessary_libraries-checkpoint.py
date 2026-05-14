import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#Basic graph

# plt.plot([[1,2,3],[2,4,6]])


df= pd.read_csv("Amazon Sale Report.csv")
df['Revenue']=df['Qty']*df['Amount']
# print(df)



top_products=df.groupby("Category")["Revenue"].sum().sort_values(ascending=False).head(5)
top_products.plot(kind="bar")

plt.title("Top 5 Product by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()


df["Date"]=pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.month
monthly_sales=df.groupby("Month")["Revenue"].sum()

monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()


df["Amount"].plot(kind="hist",bins=20)
plt.title("Price Disribution")
plt.xlabel("Price")
plt.show()


categoty_sales=df.groupby("Category")["Revenue"].sum()
categoty_sales.plot(kind="pie",autopct="%1.1f%%")
plt.title("Sales by Category")
plt.show()
