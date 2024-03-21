#!/usr/bin/env python
# coding: utf-8

# # Global Superstore

# Data Dictionary: The dataset used for model building contained 51290 observations of 24 variables. The data contains the following information:

# | Variable | Description | 
# |:---------|:--------:|
# |Row ID|	Unique identifier for each row in the dataset.|
# |Order ID|	Unique identifier for each order.|
# |Order Date|	Date the order was placed.|
# |Ship Date|	Date the order was shipped.|
# |Ship Mode|	Shipping mode for the order (e.g., standard, express).|
# |Customer ID|	Unique identifier for each customer.|
# |Customer Name|	Name of the customer.|
# |Segment|	Market segment of the customer (e.g., consumer, corporate).|
# |City|	City where the order was placed.|
# |State|	State where the order was placed.|
# |Country|	Country where the order was placed.|
# |Postal Code|	Postal code of the customer's location.|
# |Market|	Market segment (e.g., US, Europe, Asia).|
# |Region|	Region where the order was placed.|
# |Product ID|	Unique identifier for each product.|
# |Category|	Product category (e.g., office supplies, technology).|
# |Sub-Category|	Product sub-category (e.g., paper, chairs).|
# |Product Name|	Name of the product.|
# |Sales|	Total sales amount.|
# |Quantity|	Quantity of the product ordered.|
# |Discount|	Discount applied to the product.|
# |Profit|	Profit made from the order.|
# |Shipping Cost|	Cost of shipping the order.|
# |Order Priority|	Priority of the order (e.g., high, medium, low).|

# In[1]:


import pandas as pd


# In[2]:


#Loading the dataset from an CSV file
store = pd.read_csv('/Users/faizan/Desktop/Global Superstore.xls - Orders.csv')
store.head()


# In[3]:


#Checking the shape of the dataset
store.shape


# In[4]:


#Checking columns 
store.columns


# In[5]:


#Checking data types of the columns
store.info()


# In[6]:


#Checking missing values
store.isnull().sum()


# In[7]:


# Dropping missing value columns along with irrelevant columns 
store = store.drop(columns=['Row ID', 'Order ID', 'Customer ID', 'Postal Code', 'Market', 'Product ID'])


# In[9]:


store.isnull().sum()


# In[12]:


# Converting date columns to datetime format
store['Order Date'] = pd.to_datetime(store['Order Date'])
store['Ship Date'] = pd.to_datetime(store['Ship Date'])


# In[14]:


# Remove duplicates
store = store.drop_duplicates()


# In[15]:


store.info()


# In[19]:


# Export the cleaned data to a CSV file
store.to_csv('store_cleaned_data.csv', index=False)

