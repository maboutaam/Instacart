#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <b>Hello!</b> We're glad to see you in code-reviewer territory. You've done a great job on the project, but let's get to know each other and make it even better! We have our own atmosphere here and a few rules:
# 
# 
# 1. My name is Alexander Matveevsky. I work as a code reviewer, and my main goal is not to point out your mistakes, but to share my experience and help you become a data analyst.
# 2. We speak on a first-come-first-served basis.
# 3. if you want to write or ask a question, don't be shy. Just choose your color for your comment.  
# 4. this is a training project, you don't have to be afraid of making a mistake.  
# 5. You have an unlimited number of attempts to pass the project.  
# 6. Let's Go!
# 
# 
# ---
# I'll be color-coding comments, please don't delete them:
# 
# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
#     
# ---
# 
# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# Remarks. Some recommendations.
# </div>
# 
# ---
# 
# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Success. Everything is done succesfully.
# </div>
#     
# ---
#     
# I suggest that we work on the project in dialogue: if you change something in the project or respond to my comments, write about it. It will be easier for me to track changes if you highlight your comments:   
#     
# <div class="alert alert-info"> <b>Student сomments:</b> Student answer..</div>
#     
# All this will help to make the recheck of your project faster. If you have any questions about my comments, let me know, we'll figure it out together :)   
#     
# ---

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# Some blocks of code are not working. Please see what went wrong. Before submitting a project, you should check if the code works - you can do this by clicking on the Jupiter Hub Kernel and Restart & Run All panels ![image.png](attachment:image.png)

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# You cannot unload datasets in the middle of a project. It is necessary to unload only once each dataset and further work only with this variable. I've written to a tutor to help you look into this case in more detail   
#     
#     
#     
# ![image.png](attachment:image.png)

# 

# 

# The main goal of this project is to analyze and describe the shopping habits of instacart customers. This project will go through a series of steps in order to reach our goal. We will be distinguishing the most frequent time and day for shopping. In adiditon, how often do they shop and any changes between their orders. Also, we will get to know the most popular items and other facts related to their instacart shopping.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# Great!

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# An excellent practice is to describe the goal and main steps in your own words (a skill that will help a lot on a final project). It would be good to add the progress and purpose of the study.

# ### The goal of this project is to clean the data from any duplications and missing values in order to filter the data, visualize it clearly, and have a better understanding about the customer's shopping habbits which would help Instacart and the grocery stores to focus on the negatives and resolve them in order to grow in the market. 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# data opening
df_instacart_orders = pd.read_csv("/datasets/instacart_orders.csv", delimiter = ";")
# working code
df_instacart_orders.info()
df_instacart_orders.head()


# In[3]:


# data opening 
df_products = pd.read_csv("/datasets/products.csv", delimiter = ";")
#working code
df_products.info()
df_products.head()


# In[4]:


# data opening
df_order_products = pd.read_csv("/datasets/order_products.csv", delimiter = ";")
# working code
df_order_products.info()
df_order_products.head()


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# I suggest separating logically different things:
# 
# 
#     - data opening (this may not be a trivial process)
#     - working code
#     
# This approach will improve code readability, reduce the time of searching for errors, if there are any, and exclude code re-execution
# </div>

# In[5]:


# data opening
df_aisles = pd.read_csv("/datasets/aisles.csv", delimiter = ";")
# working code
df_aisles.info()
df_aisles.head()


# In[6]:


# data opening
df_departments = pd.read_csv("/datasets/departments.csv", delimiter = ";")
# working code
df_departments.info()
df_departments.head()


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# No familiarity with the data (use info() and head() methods

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# It would be good to comment on the data somehow

# # 478966 orders, 49694 products, 4545007order products, 134 aisles, 21 departments.

# ## Find and remove duplicate values (and describe why you make your choices)

# ### `orders` data frame

# In[7]:


# working code
df_instacart_orders.duplicated().sum()


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# I suggest separating logically different things:
# 
#     - library imports
#     - data opening (this may not be a trivial process)
#     - working code
#     
# This approach will improve code readability, reduce the time of searching for errors, if there are any, and exclude code re-execution
# </div>

# 

# 

# In[8]:


#working code
df_instacart_orders.head()


# In[9]:


# Check for all orders placed Wednesday at 2:00 AM

wednesday_2am_orders = df_instacart_orders[
    (df_instacart_orders['order_dow'] == 4 ) & 
    (df_instacart_orders['order_hour_of_day'] == 2 )
]

print(wednesday_2am_orders)


# In[10]:


# Remove duplicate orders
#working code
df_instacart_orders.drop_duplicates()


# In[11]:


# Double check for duplicate rows

#working code
df_instacart_orders[df_instacart_orders.duplicated()]


# In[12]:


# Double check for duplicate order IDs only

# working code
df_instacart_orders[df_instacart_orders.duplicated(subset=['order_id'])]


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Duplicate checking is the basis of data preprocessing

# 

# ### `products` data frame

# In[13]:


#working code
df_products.head()


# In[14]:


# Check for fully duplicate rows

#working code
df_products.duplicated().any()


# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# It's more efficient to load datasets once at the beginning of your project and then work with those loaded datasets throughout your analysis. Loading the same dataset repeatedly can be time-consuming and unnecessary. By loading the datasets only once at the start of the project, you can optimize your workflow and avoid redundant operations. Consider loading your datasets at the beginning and then utilizing them for all subsequent analysis to streamline your work and improve efficiency

# In[15]:


# Check for just duplicate product IDs

#working code
df_products['product_id'].duplicated().any()


# In[16]:


# Check for just duplicate product names (convert names to lowercase to compare better)

# working code
df_products['product_name'].str.lower()


# In[17]:


df_products[df_products.duplicated(subset=['product_name'], keep=False)]


# In[18]:


# Check for duplicate product names that aren't missing

#working code
df_products.dropna(subset=['product_name'])


# 

# ### `departments` data frame

# In[19]:


#working code
df_departments.head()


# In[20]:


#working code
df_departments.duplicated().any()


# 

# ### `aisles` data frame

# In[21]:


# working code
df_aisles.duplicated().sum()


# There are no duplictates.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# Correct

# ### `order_products` data frame

# In[22]:


# working code
df_order_products.head()


# In[23]:


# Check for fullly duplicate rows

#working code
df_order_products.duplicated().sum()


# In[24]:


# Double check for any other tricky duplicates

#working code
df_order_products.duplicated().any()


# In[25]:


#working code
df_products['product_id'].duplicated().any().sum()


# In[26]:


df_instacart_orders['order_id'].duplicated().any().sum()


# In[27]:


df_order_products.head()


# In[28]:


df_order_products.duplicated(subset=['order_id', 'product_id'])


# In[29]:


df_order_products[df_order_products.duplicated(subset=['order_id', 'product_id'])]


# In[30]:


duplicates_check = df_order_products[df_order_products.duplicated(subset=['order_id', 'product_id'])]
print(duplicates_check)


# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# We need to check for duplicate columns: 'order_id` and 'product_id'

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №4__
# 
# 
# 
# Can you please look at an example
#     
#     order_products[order_products.duplicated(subset=['order_id', 'product_id'])]

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №5__
# 
# Now correct

# ## Find and remove missing values
# 

# ### `products` data frame

# In[31]:


# working code
df_products.head()


# In[32]:


# Are all of the missing product names associated with aisle ID 100?

# working code
df_products['aisle_id'].eq(100).all()


# In[33]:


# Are all of the missing product names associated with department ID 21?

# working code
df_products['department_id'].eq(21).all()


# In[34]:


# What is this ailse and department?

# working code
df_aisles.loc[df_aisles['aisle_id'] == 100, 'aisle'].iloc[0]


# In[35]:


# What is this ailse and department?
df_departments.loc[df_departments['department_id'] == 21, 'department'].iloc[0]


# In[36]:


# Fill missing product names with 'Unknown'

# working code
df_products['product_name'] = df_products['product_name'].fillna('Unknown')


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# No variable overwrite (df = df[].fillna())

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №4__
# 
# You chose the most correct way to replace the omissions in the categorical column. Well done!)

# ### `orders` data frame

# In[37]:


# working code
df_instacart_orders.head()


# In[38]:


# Are there any missing values where it's not a customer's first order?

# working code
df_instacart_orders.duplicated(subset='user_id', keep='first')


# 

# ### `order_products` data frame

# In[39]:


# working code
df_order_products.head()


# In[40]:


# What are the min and max values in this column?

# working code
df_order_products.min()


# In[41]:


# What are the min and max values in this column?

# working code
df_order_products.max()


# In[42]:


# Save all order IDs with at least one missing value in 'add_to_cart_order'

# working code
orders_with_missing_values = df_order_products.loc[df_order_products['add_to_cart_order'].isnull(), 'order_id'].unique()
order_ids_with_missing_values = orders_with_missing_values.tolist()

print("Order IDs with at least one missing value in 'add_to_cart_order':")
print(order_ids_with_missing_values)


# In[43]:


# Do all orders with missing values have more than 64 products?

# working code
orders_with_missing_values = df_order_products[df_order_products['add_to_cart_order'].isnull()]
order_product_counts = orders_with_missing_values.groupby('order_id').size()
all_more_than_64 = all(order_product_counts > 64)

if all_more_than_64:
    print("All orders with missing values have more than 64 products.")
else:
    print("Not all orders with missing values have more than 64 products.")


# In[44]:


# Replace missing values with 999 and convert column to integer type

# working code
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].fillna(999)
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].astype(int)

print(df_order_products.head())


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №3__
# 
# 
# Replacing it with 999/-1 etc is not really good. Tip for the future, look, it's not good to try to fill in the blanks left and right. In real work - replace with zero now, then forget and average count a month later. Plus there may be times when a bonus purchase or gift, will cost zero. In general, if it is possible to leave skips as skips - and here it can be done, it is better to do so, the results, even if we want to calculate something - it will not affect the results
# 
# It is better to use this code construction:
#     
#     data[''] = data[''].astype('Int64', errors='ignore')
# </div>

# 

# # [A] Easy (must complete all to pass)

# ### [A1] Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)

# In[45]:


# working code
df_instacart_orders.head()


# In[46]:


# working code
# order_dow
df_instacart_orders["order_dow"].sort_values().unique()


# In[47]:


# working code
df_instacart_orders["order_hour_of_day"].sort_values().unique()


# ### [A2] What time of day do people shop for groceries?

# In[48]:


# Working Code
df_instacart_orders['order_hour_of_day'].sort_index()


# In[49]:


# working code
order_hours = df_instacart_orders['order_hour_of_day']

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(order_hours, bins=24, color='skyblue', edgecolor='black')
plt.title('Distribution of Orders by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[50]:


# working code
df_instacart_orders['order_hour_of_day'].value_counts()


# In[51]:


# working code
order_hours = df_instacart_orders['order_hour_of_day'].value_counts().sort_index()

# Plot the hour with the highest frequency of orders
order_hours.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Frequency of Orders by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# There is a lack of visualization. Can you please add

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №4__
# 
# missing visualization. Can you please add

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №5__
# 
# Well done

# 

# In[52]:


# Find the hour with the highest frequency of orders
df_instacart_orders.groupby(['order_hour_of_day']).count()


# In[53]:


# Find the hour with the highest frequency of orders
# working code
order_frequency_by_hour = df_instacart_orders.groupby(['order_hour_of_day'])['order_hour_of_day'].count()

# Plot the hour with the highest frequency of orders
plt.figure(figsize=(10, 6))
order_frequency_by_hour.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Frequency of Orders by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# ## We can conclude from the above bar graph that the highest number of orders is at 10 AM. This was interpreted as a result of the highest number of orders 40578 was recorded at 10 am. This means that customers are most likely to go grocery shopping in the morning hours. 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# It is better after each section, graph (or series of tests) to write a conclusion on the obtained data taking into account the set business task - so it is easier to read the project, because future colleagues or customers will not have to interpret the results of each section, test or graph themselves.

# In[54]:


# Working Code
hourly_order_counts = df_instacart_orders['order_hour_of_day'].value_counts().sort_index()
peak_hour = hourly_order_counts.idxmax()
peak_order_count = hourly_order_counts.max()

print(f"The peak hour for shopping groceries is {peak_hour} with {peak_order_count} orders.")


# 

# ### [A3] What day of the week do people shop for groceries?

# In[55]:


# Data Opening
df_instacart_orders['order_dow'].head()


# In[56]:


# Working Code
order_counts_by_day = df_instacart_orders.groupby(['order_dow'])['order_dow'].count()
total_orders_on_most_popular_day = order_counts_by_day.max()
most_popular_day = order_counts_by_day.idxmax()

print(f"The most popular day for shopping groceries is day {most_popular_day} "f"with {total_orders_on_most_popular_day} orders.")


# 

# ### [A4] How long do people wait until placing another order?

# In[57]:


# Working Code
df_instacart_orders['days_since_prior_order']


# In[58]:


# Working Code
mean_wait_time = df_instacart_orders['days_since_prior_order'].mean()
median_wait_time = df_instacart_orders['days_since_prior_order'].median()
mode_wait_time = df_instacart_orders['days_since_prior_order'].mode()[0]

print(f"Mean wait time between orders: {mean_wait_time:.2f} days")
print(f"Median wait time between orders: {median_wait_time} days")
print(f"Mode wait time between orders: {mode_wait_time} days")


# 

# # [B] Medium (must complete all to pass)

# ### [B1] Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.

# In[59]:


# working code
df_instacart_orders['order_hour_of_day']


# In[60]:


# working code
df_instacart_orders['order_dow']


# In[61]:


# working code
wednesday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 3]  # Wednesday is represented by 3
saturday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 5]   # Saturday is represented by 5

# Plot histograms for 'order_hour_of_day' for Wednesdays and Saturdays
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(wednesday_orders['order_hour_of_day'], bins=24, color='skyblue', edgecolor='black')
plt.title('Wednesday')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
plt.hist(saturday_orders['order_hour_of_day'], bins=24, color='lightgreen', edgecolor='black')
plt.title('Saturday')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


# ##  The number of orders per hour on Saturday are higher than the number of orders on Wednesday. This means that customers are more likely to go grocery shopping on weekends.

# 

# ### [B2] What's the distribution for the number of orders per customer?

# In[62]:


# data opening
df_instacart_orders['user_id']


# In[63]:


# data opening
df_instacart_orders.groupby('user_id').size()


# In[64]:


merged_df = pd.merge(df_instacart_orders, df_order_products, on="order_id", how="inner")

# Group orders by customer ID and count the number of orders for each customer
orders_per_customer = merged_df.groupby('user_id')['order_id'].nunique()

# Plot the distribution of the number of orders per customer
plt.figure(figsize=(10, 6))
plt.hist(orders_per_customer, bins=max(orders_per_customer), color='skyblue', edgecolor='black')
plt.title('Distribution of Number of Orders per Customer')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# 

# ### [B3] What are the top 20 popular products (display their id and name)?

# In[65]:


# working code
merged_data = pd.merge(df_instacart_orders, df_products, how='inner', left_on='order_number', right_on='product_id')

# Group by product_id and count occurrences to find out how many times each product appears in orders
product_counts = merged_data['product_id'].value_counts()

# Get the top 20 most frequently ordered products
top_20_product_counts = product_counts.head(20)

# Filter product details for the top 20 products
top_20_popular_products = df_products[df_products['product_id'].isin(top_20_product_counts.index)]
print(top_20_popular_products)


# In[66]:


# working code
df_instacart_orders.head()


# In[67]:


# Data Loading
merged_data_1 = pd.merge(df_instacart_orders, df_order_products, on = 'order_id')
merged_data = pd.merge(merged_data_1, df_products, how='inner', left_on='product_id', right_on='product_id')
popular_products = merged_data.groupby(['product_id', 'product_name'])['department_id'].count().reset_index()
popular_products = popular_products.rename(columns = {'department_id':'order_count'})

# Data Loading
popular_products = popular_products.sort_values(by='order_count', ascending=False)

# Working code
top_20_popular_products = popular_products.head(20)

print(top_20_popular_products[['product_id', 'product_name']])


# In[68]:


# data loading
df_products['product_id']


# In[69]:


# working code
merged_data_1 = pd.merge(df_instacart_orders, df_order_products, on = 'order_id')
merged_data = pd.merge(merged_data_1, df_products, how='inner', left_on='product_id', right_on='product_id')
popular_products = merged_data.groupby(['product_id', 'product_name'])['department_id'].count().reset_index()
popular_products = popular_products.rename(columns = {'department_id':'order_count'})

# Plot the distribution of the top 20 popular products
plt.barh(top_20_popular_products['product_name'], top_20_product_counts, color='skyblue')
plt.xlabel('Number of Orders')
plt.ylabel('Product')
plt.title('Top 20 Popular Products')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# ### The Top 20 products that customers are mostly organic produce, vegetables and fruits. This means that these products are bestsellers and popular among customers.

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# There is a lack of visualization. Can you please add

# # [C] Hard (must complete at least two to pass)

# ### [C1] How many items do people typically buy in one order? What does the distribution look like?

# In[70]:


# working code
items_per_order = df_order_products.groupby('order_id')['product_id'].count()
print(items_per_order)


# In[71]:


# Sample data to demonstrate the visualization

# Plot the distribution of items per Order
plt.figure(figsize=(10, 6))
plt.hist(items_per_order, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Number of Items per Order')
plt.ylabel('Frequency')
plt.title('Distribution of Items per Order')
plt.grid(True)
plt.show()


# 

# ### [C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# In[72]:


df_order_products['reordered'].head()


# In[73]:


# working code
reorder_frequency = df_order_products.groupby('product_id')['reordered'].sum().reset_index(name='reorder_count')
top_reordered_products = pd.merge(reorder_frequency, df_products[['product_id', 'product_name']], on='product_id')
top_reordered_products = top_reordered_products.sort_values(by='reorder_count', ascending=False)

print(top_reordered_products.head(20)[['product_id', 'product_name']])


# In[ ]:





# In[ ]:





# 

# ### [C3] For each product, what proportion of its orders are reorders?

# In[74]:


# working code
product_reorder_proportion = df_order_products.groupby('product_id')['reordered'].mean().reset_index()

product_reorder_proportion.columns = ['product_id', 'reorder_proportion']

print(product_reorder_proportion)


# In[ ]:





# In[ ]:





# ### [C4] For each customer, what proportion of their products ordered are reorders?

# In[75]:


# working code
merged_df = pd.merge(df_instacart_orders, df_order_products, on="order_id", how="inner")

customer_reorder_proportion = merged_df.groupby('user_id')['reordered'].mean().reset_index()

customer_reorder_proportion.columns = ['user_id', 'reorder_proportion']

print(customer_reorder_proportion)


# ### [C5] What are the top 20 items that people put in their carts first? 

# In[76]:


#working code
top_first_items = df_order_products[df_order_products['add_to_cart_order'] == 1].groupby('product_id')['add_to_cart_order'].count().sort_values().head(21)

top_first_items_with_names = pd.merge(top_first_items, df_products, on="product_id", how="left")

print(top_first_items_with_names[['product_id', 'product_name' , 'add_to_cart_order']])


# ## After properly filtering all the data and visualizing the results. We can understand that customers are more likely to go grocery shopping on Saturday than any other day of the week. Also, they would prefer to go in the morning hours such as 10 AM. In addition, organic products and produce are highly popular among customers because they are the top 20 bestsellers. 

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №4__
# 
# All right

# 

# 

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №3__
# 
# 
# It would be nice to add an overall output for the projec
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №5__
# 
# 
# Otherwise it's great😊. Your project is begging for github =)   
#     
# Congratulations on the successful completion of the project 😊👍
# And I wish you success in new works 😊
