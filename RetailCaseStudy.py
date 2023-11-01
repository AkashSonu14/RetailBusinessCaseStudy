import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Customer=pd.read_csv('E:\Files\Pandas Case Study 1 - Retail Case Study\Customer.csv')
Transaction=pd.read_csv('E:\Files\Pandas Case Study 1 - Retail Case Study\Transactions.csv')
Prod_cat_info=pd.read_csv('E:\Files\Pandas Case Study 1 - Retail Case Study\Prod_cat_info.csv')

# 1. Merging the Files

#     merging Customer and Transactions and saved in Cust_Trans
Cust_Trans = pd.merge(left = Customer,right = Transaction,left_on = 'customer_Id',right_on = 'cust_id', how = 'inner',indicator = True)
#     merging Cust_Trans and Prod_cat_info then saved in Cust_Final
Cust_Final = pd.merge(left = Cust_Trans,right = Prod_cat_info,left_on = 'prod_cat_code',right_on = 'prod_cat_code',how = 'inner')

'''a= 'E:\Files\Pandas Case Study 1 - Retail Case Study\Cust_Final.csv'
Cust_Final.to_csv(a, index=False)'''

# 2. Summary Report

#     Column names with their data-types
print(Cust_Final.dtypes)
#     Top/Bottom 10 Observations
print(Cust_Final.head(10))
print(Cust_Final.tail(10))
#     Five-number summary for continuous variables (min, Q1, median, Q3 and max)
Data_min = Cust_Final['total_amt'].min()
Data_max = Cust_Final['total_amt'].max()
Data_q1  = np.percentile(Cust_Final.total_amt,25)
median  = np.percentile(Cust_Final.total_amt,50)
Data_q3  = np.percentile(Cust_Final.total_amt,75)
print('Minimum = ',Data_min)
print('Maximum = ',Data_max)
print('Median = ',median)
print('Q1 = ',Data_q1)
print('Q3 = ',Data_q3)

# 3. Generate histograms for all continuous variables and frequency bars for categorical variables

   # Histogram

   # Frequency Bars
          # For Store Type
Val1= Cust_Final.groupby('Store_type')['total_amt'].sum().reset_index()
plt.bar(Val1['Store_type'],Val1['total_amt'])
plt.xlabel('Store Type')
plt.ylabel('Total Amount')
plt.title('Total Amount by Store Type')
plt.show()

          # For Sub Category
Val2= Cust_Final.groupby('prod_subcat')['total_amt'].sum().reset_index()
plt.bar(Val2['prod_subcat'],Val2['total_amt'])
plt.xlabel('Product Sub Category')
plt.ylabel('Total Amount')
plt.title('Total Amount by Product Sub Category')
plt.xticks(rotation=45)
plt.show()

          # For Gender
Val3= Cust_Final.groupby('Gender')['Qty'].count().reset_index()
plt.bar(Val3['Gender'],Val3['Qty'])
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.title('Total Amount by Product Sub Category')
plt.show()

# 4. Using Merged Dataset

   # a. Time period of the available transaction data

   # b. Count of transactions where the total amount of transaction was negative
df = Cust_Final['total_amt']
count_neg= Cust_Final.loc[(df<0),['total_amt']].count()
print("count of negative",count_neg)

# 5.

    # Popular among Male
M = Cust_Final.loc[Cust_Final['Gender']=='M']
group_prod = M.groupby(['prod_cat'])['total_amt'].sum()
popular_M = group_prod.nlargest(1)
print('The most popular product category in Male customers is : ',popular_M)

    # Popular among Female
F = Cust_Final.loc[Cust_Final['Gender']=='F']
group_prod1 = F.groupby(['prod_cat'])['total_amt'].sum()
popular_F = group_prod1.nlargest(1)
print('The most popular product category in Female customers is : ',popular_F)

# 6. Which City code has the maximum customers and what was the percentage of customers from that city

max_cust = Customer['city_code'].value_counts()
t = max_cust.nlargest(1)
print("City code which has Maximum customers is : ",t)
tot_customer = Customer['customer_Id'].count()
percent = round((t/tot_customer)*100,2)
print("Percentage of customers is ",percent)

# 7. Which store type sells the maximum products by value and by quantity

sort_list = Cust_Final.sort_values(['total_amt','Qty'],ascending = False)
print(sort_list.head(1)['Store_type'])

# 8. What was the total amount earned from the "Electronics" and "Clothing" categories from Flagship Stores

dt = pd.DataFrame(Cust_Final)
tf = dt[dt.prod_cat.isin(['Electronics','Clothing']) & (dt.Store_type == 'Flagship store')]
total = tf.total_amt.sum()
print('Total amount earned',total)

# 9. What was the total amount earned from "Male" customers under the "Electronics" category

dh = pd.DataFrame(Cust_Final)
tf1 = dh[(dh.Gender == 'M') & (dh.prod_cat == 'Electronics')]
total = tf1.total_amt.sum()
print('Total amount earned in Electronics by male :',total)

# 10. How many customers have more than 10 unique transactions, after removing all transactions which have any negative amounts

dl = pd.DataFrame(Cust_Final)
df1 = dl[(dl.total_amt > 0)]
ts = df1.transaction_id.nunique()
print('Total customers having more than 10 unique transactions are : ',ts)

print("sucess")
print("fkysegfe")


