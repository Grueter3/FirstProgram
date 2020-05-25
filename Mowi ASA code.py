import numpy as np
Year= [2016, 2017, 2018, 2019, 'TTM',]
Ydict = {'TTM':'0', '2019':'1', '2018':'2', '2017':'3', '2016':'4'}
 
#Total Revenue    
TotalRevenue = np.array([350280000, 362610000, 374980000, 407420000, 397880000])                      
TotalRevdict = {'TTM': '397880000','2019':'407420000','2018':'374980000','2017':'362610000','2016':'350280000'}

#Cost of Revenue
CostofRevenue = np.array([52640000,202880000,166580000,211030000,28750000])
CostofRevdict = {'TTM':'28750000','2019':'211030000','2018':'166580000','2017':'202880000','2016':'52640000'}                

#Gross Profit
GrossProfit= np.array([297640000,159730000,208400000,196390000,169130000])
GrossProfdict = {'TTM':'169130000','2019':'196390000','2018':'208400000','2017':'159730000','2016':'297640000'}                

#Profit Margin
#Gross profit / Total Revenue = Profit Margin
ProfitMargin = np.round(GrossProfit / TotalRevenue,2)*100 
ProfitMargin = np.array([85.,44.,56.,48.,43.])
ProftiMargdict = {'TTM': 43., '2019': 48., '2018': 56., '2017': 44., '2016': 85.}

#Percentage of Total Operating Expenses
#Total Operating Expenses / Gross Profit = Percentage of Total Operating Expenses

TotalOperatingExpenses = np.array([139520000,136950000,119240000,104010000,115620000])
TotalOperatingExpenses = TotalOperatingExpenses[::-1]
TotalOpExpPercent = np.round(TotalOperatingExpenses / GrossProfit,5)*100 

GrossProfit = np.array([169130000,196390000,208400000,159730000,297640000])
GrossProfit = GrossProfit[::-1]
GrossProfit1 = GrossProfit[:4]

#Depreciation (cap equip./investment) / GrossProfit = Depreciation as a Percent of GrossProfit
Depreciation = np.array([2916000,1644000,2542000,1602000])
Depreciation = Depreciation[::-1]
DepreciationPercentofGP = np.round(Depreciation / GrossProfit1,5)*100
Year1 = [2016, 2017, 2018, 2019,] #No TTM for this graph

#Interest Expense / Operating Income = Percent Operating Income Paid out as Interest
InterestExpense = np.array([7590000,7020000,5000000,4670000,4840000])
InterestExpense = InterestExpense[::-1]
InterestExpPercent= np.round(InterestExpense / GrossProfit,5)*100

#---------------------------------------------------------------------------------------

#Graphs
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

plt.plot((TotalOpExpPercent),c = 'green', ls = '--', marker = 's', ms = 7, Label= 'TotalOpExPercent')
plt.xticks(list(range(0,5)), Year, rotation = 'vertical')
plt.rcParams['figure.figsize'] = 8,4
plt.legend(loc='upper right')
plt.xlabel('Year')
plt.ylabel('')
plt.title('Total Operating Expense Percent')

#Profit Margin

import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

plt.plot((ProfitMargin),c = 'red', ls = '--', marker = 'o', ms = 7, Label= 'Profit Margin') 
plt.xticks(list(range(0,5)), Year, rotation = 'vertical')
plt.rcParams['figure.figsize'] = 8,4
plt.legend(loc='upper right', bbox_to_anchor=(1.1,1.2))
plt.xlabel('Year')
plt.ylabel('Percent')
plt.title('Profit Margin')
plt.show()

#Depreciation as Percent of Gross Prifit
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

plt.plot((DepreciationPercentofGP),c = 'blue', ls = '--', marker = 'd', ms = 7, Label= 'DepreciationPercentofGP')
plt.xticks(list(range(0,4)), Year, rotation = 'vertical')
plt.rcParams['figure.figsize'] = 8,4
plt.legend(loc='upper right', bbox_to_anchor=(1.1,1.2))
plt.xlabel('Year')
plt.ylabel('Percent')
plt.title('Depreciation as a Percent of Gross Profit')
plt.show()

# Interest Expense Percent
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

plt.plot((InterestExpPercent),c = 'violet', ls = '--', marker = 's', ms = 7, Label= 'Interest Expense Percent')
plt.xticks(list(range(0,5)), Year, rotation = 'vertical')
plt.rcParams['figure.figsize'] = 8,4
plt.legend(loc='upper right', bbox_to_anchor=(1.1,1.2))
plt.xlabel('Year')
plt.ylabel('Percent')
plt.title('Interest Expense Percent')
plt.show()

#----------------------------------------------------------------------------------

#NOTES:
# Look Selling/General/Administrative Expenses (SGA) in relation to Gross Profit = low is better
# Operating Expenses + R&D Expenses / Gross Profit = low is better
#Interest Expense = the Interest Paid out at each quarter reflecting total debt of company
