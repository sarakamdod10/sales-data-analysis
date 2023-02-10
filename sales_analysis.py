import pandas as pd
import matplotlib.pyplot as plt
import os

sales_path = '/content/Sales'
file_names = os.listdir(sales_path)

yearly_sales = pd.DataFrame()

for file in file_names:
    temp_dataframe = pd.read_csv(sales_path+"/"+file)
    yearly_sales = pd.concat([yearly_sales,temp_dataframe])
print(yearly_sales.head())
print(yearly_sales.shape)

#NaN data
yearly_sales[yearly_sales.isna().any(axis=1)] #if whole row in NaN

print(yearly_sales.shape)
yearly_sales = yearly_sales.dropna(how = 'all')
print(yearly_sales.shape)

yearly_sales.dtypes

yearly_sales.head()

print(yearly_sales.shape)
yearly_sales = yearly_sales[yearly_sales['Quantity Ordered'].str[0:1]!='Q']
print(yearly_sales.shape)

yearly_sales.dtypes

yearly_sales['Quantity Ordered'] = pd.to_numeric(yearly_sales['Quantity Ordered'])

yearly_sales.dtypes

yearly_sales['Order ID'] = pd.to_numeric(yearly_sales['Order ID'])

yearly_sales.dtypes

yearly_sales['Price Each'] = pd.to_numeric(yearly_sales['Price Each'])

yearly_sales.dtypes

yearly_sales['Product'] = yearly_sales['Product'].astype(str)

yearly_sales.dtypes

yearly_sales['Month'] = yearly_sales['Order Date'].str[0:2].astype('int8') #Index 0 and 1

yearly_sales.tail()

def get_city(purchase_address): 
    return purchase_address.split(",")[1].strip(" ")

yearly_sales['city'] = yearly_sales['Purchase Address'].apply(get_city)

yearly_sales

def get_state(purchase_address): 
    return purchase_address.split(",")[2].split(" ")[1]

yearly_sales['State'] = yearly_sales['Purchase Address'].apply(get_state)

yearly_sales.head()

#Which month has the least sales and which month has the most sales?

#Multiply Quantity Order and Price Each to create new column called Sales
#Group By Month and print Sales part

yearly_sales['Sales'] = yearly_sales['Quantity Ordered']*yearly_sales['Price Each']

yearly_sales.head()

yearly_sales.groupby(['Month']).sum()

#Instead of printing Sales monthly in table,
#Show it in a bar graph
plt.bar(range(1,13),yearly_sales.groupby(['Month']).sum()['Sales'])
plt.xticks(range(1,13))
plt.ylabel('Sales in USD')
plt.xlabel('Month in Number')
plt.show()

#Show sales per city (Pie Chart?)
#Show sales per city (Bar Graph?)

yearly_sales.groupby(['city']).sum()

cities = yearly_sales['city'].unique()
cities.sort()
print(cities)
plt.bar(cities,yearly_sales.groupby(['city']).sum()['Sales'])
plt.xticks(cities,rotation='vertical')
plt.ylabel('Sales in USD')
plt.xlabel('City')
plt.show()

cities = yearly_sales['city'].unique()
cities.sort()
print(cities)
plt.pie(yearly_sales.groupby(['city']).sum()['Sales'],labels=cities)
plt.show()

The company wants to find out which is the right time to put advertisements on television.

Can you help by analyzing the data and figuring out during which hour most sales are done?

Print as a grid plot

yearly_sales['Hour'] = pd.to_datetime(yearly_sales['Order Date']).dt.hour

yearly_sales['Minute'] = pd.to_datetime(yearly_sales['Order Date']).dt.minute

yearly_sales.head()

plt.plot(range(0,24),yearly_sales.groupby(['Hour']).count()['Order ID'])

plt.xticks(range(0,24))
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.title("Number of Orders Per Hour")
plt.show()

plt.plot(range(0,24),yearly_sales.groupby(['Hour']).sum()['Sales'])
plt.xticks(range(0,24))
plt.xlabel("Hour")
plt.ylabel("Sales")
plt.title("Sales Per Hour")
plt.show()

Which products are sold the most?

yearly_sales.groupby(['Product']).sum()

products = yearly_sales['Product'].unique()
products.sort()
print(products)
plt.bar(products,yearly_sales.groupby(['Product']).sum()['Quantity Ordered'])
plt.xticks(products,rotation='vertical')
plt.ylabel('Quantity Sold')
plt.xlabel('Product')
plt.show()

Find out which products are bought together the most? 

The company wants to run offers on these combo products

mul_orders = yearly_sales[yearly_sales['Order ID'].duplicated(keep=False)]

#Take the above data and find a way to print most commonly bought products
