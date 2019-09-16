import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 
with open(path) as f:
    read_data=csv.reader(f,delimiter =",")
    read_data=list(read_data)
#remove the header

read_data.remove(read_data[0])
# Convert the data into a numpy array and store it in sales_data
sales_data=np.array(read_data)

# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter
unique_add_campaign=print(np.unique(sales_data[:,1])) 
print(Counter(sales_data[:,1]))

# What are the age groups that were targeted through these ad campaigns?
age_groups=np.unique(sales_data[:,3])
print("Age groups that were targeted",age_groups)

# What was the average, minimum and maximum amount spent on the ads?
Min_Amt=sales_data[:,8].astype(float).min()
Max_Amt=sales_data[:,8].astype(float).max()
Average_Amt=sales_data[:,8].astype(float).mean()
print("average, minimum and maximum amount spent on the ads",Average_Amt,Min_Amt,Max_Amt,"respectively")
print(sales_data[:,8].astype(float))

# What is the id of the ad having the maximum number of clicks ?
max_clicks_idadd=sales_data[:,7].astype(float).max()
print(max_clicks_idadd)
mask=(sales_data[:,7].astype(float)==max_clicks_idadd)
ad_id_max_clicks=sales_data[:,0][mask]
print('id of the ad having the maximum number of clicks',ad_id_max_clicks)

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
mask_1=(sales_data[:,0]==ad_id_max_clicks)
people_bought=sales_data[:,10][mask_1]
print("people bought the product after seeing the ad with most clicks",people_bought) 

# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases
max_purchases=sales_data[:,-1].astype(int).max()
print(sales_data[:,-1].astype(int).max()==max_purchases)
print("product having maximum number of purchases",max_purchases)

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 

# Create a new numpy array to calculate CTR
CTR = np.array((sales_data[:,7].astype(float)/sales_data[:,6].astype(float))*100)

# Note the shapes of CTR and the original array are different
print(sales_data.shape)
print('The original shape of CTR is ',CTR.shape)

# Convert CTR to the same shape as that of the original array
CTR = CTR.reshape(-1,1)
print('New shape of CTR is ',CTR.shape)

# Concatenate CTR to the original array
sales_data = np.concatenate((sales_data, CTR),axis=1)
sales_data

# Create a new column that represents Cost Per Mille (CPM) 


# Create a new numpy array to calculate CPM
CPM = (sales_data[:,8].astype(float)/sales_data[:,6].astype(float))*1000

# Note the shapes of CPM and the original array are different
print(sales_data.shape)
print('The original shape of CPM is ',CPM.shape)

# Convert CTR to the same shape as that of the original array
CPM = CPM.reshape(-1,1)
print('New shape of CTR is ',CPM.shape)

# Concatenate CTR to the original array
sales_data = np.concatenate((sales_data, CPM),axis=1)
print(sales_data)
