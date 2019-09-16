# --------------
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
print(read_data)
#print(f.read())


# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter

    


# What are the age groups that were targeted through these ad campaigns?

# What was the average, minimum and maximum amount spent on the ads?

# What is the id of the ad having the maximum number of clicks ?

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
 
# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 



# Create a new column that represents Cost Per Mille (CPM) 





