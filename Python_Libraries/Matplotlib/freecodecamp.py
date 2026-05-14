import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Basic Graph
x=[0,1,2,3,4]
y=[0,2,4,6,8]
x2=np.arange(0,4.5,0.5)

# plt.figure(figsize=(5,3),dpi=300)

# plt.plot([1,2,3,4,2,3],[23,4,33,3,4,6],label="3x",color='yellow',marker='.',markersize=10)
# plt.plot(x,y,'b--',label="2x")
# plt.plot(x2[:6],x2[:6]**2,'r--',label="x**2")
# plt.title("First graph",fontdict={'fontname':'Comic sans MS','fontsize':20})
# plt.xlabel("x",fontdict={'fontsize':20})
# plt.ylabel("y")
# plt.xticks([0,2,3,4,5,6])
# plt.yticks([0,1,4,6,8,10,15,20])
# plt.legend()
# # plt.savefig("new.png")
# plt.show()

# labels=['A','B','C']
# values=[1,4,2]
# plt.figure(figsize=(6,4))
# bars=plt.bar(labels,values)
# # bar[0].set_hatch('/')
# # bar[1].set_hatch('*')
# # bar[2].set_hatch('o')
# patterns=['/','o','*']
# for bar in bars:
#     bar.set_hatch(patterns.pop(0))
# plt.show()


# gas=pd.read_csv('gas_prices.csv')
# plt.figure(figsize=(8,5))
# plt.title('Gas Prices over Time (in USD)')
# plt.xlabel("Year")
# plt.ylabel("Price")
# # plt.plot(gas.Year,gas.USA,'b.-',label="USA")
# # plt.plot(gas.Year,gas.Canada,'r.-',label="Canada")
# # plt.plot(gas.Year,gas['South Korea'],'y.-',label="South Korea")
# # plt.plot(gas.Year,gas.Australia,'g.-',label="Australia")
# # print(gas.columns)
# for country in gas:
#     if country != 'Year':
#         plt.plot(gas.Year,gas[country],marker='.',label=country)
# plt.xticks(gas.Year[::3])

# plt.legend()
# # plt.figure(figsize=())
# # print(gas)
# plt.show()


bins=[0,10,20,30,40,50,60,70,80,90,100]
fifa=pd.read_csv("fifa_data.csv")
print(fifa)

plt.hist(fifa.Overall,bins)
plt.xticks(bins)
plt.show()

left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]

right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]

plt.pie([left,right])
plt.show()