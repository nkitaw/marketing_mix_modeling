datasets

#Install libraries
#pip install numpy 

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Bringing in data
input_data_a = datasets[0]

#Filtering only on division A
input_data_a = input_data_a.loc[input_data_a['division'] == 'A']

#Dropping unneeded columns like the division, organic views, and views
input_data_b = input_data_a.iloc[:,[1,2,4,6,7,9]]

#Creating new total impression column
input_data_b['total_impressions'] = input_data_b['paid_views'] + input_data_b['google_impressions'] + input_data_b['facebook_impressions'] + input_data_b['affiliate_impressions']

#Creating ROI Column
input_data_b['roi_overall'] = input_data_b['sales'] / input_data_b['total_impressions']

###########%% Creating overall impressions plot%%################

#Creating inputs for plot
X = input_data_b['total_impressions']
Y = input_data_b['sales']
Z = input_data_b['roi_overall']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('sales', color = color)
ax1.scatter(X, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(X,Z, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('Spend Response Curve vs ROI Curve', fontweight ="bold")
 
# Show plot
plt.show()


########################## Creating FB response/ROI Curve########
input_data_b['roi_fb'] = input_data_b['sales'] / input_data_b['facebook_impressions']

#Creating inputs for plot
A = input_data_b['facebook_impressions']
Y = input_data_b['sales']
B = input_data_b['roi_fb']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('Sales', color = color)
ax1.scatter(A, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(A,B, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('FB Spend Response Curve vs ROI Curve', fontweight ="bold")
 
# Show plot
plt.show()

########################## Creating Google response/ROI Curve########
input_data_b['roi_google'] = input_data_b['sales'] / input_data_b['google_impressions']

#Creating inputs for plot
A = input_data_b['google_impressions']
Y = input_data_b['sales']
B = input_data_b['roi_google']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('Sales', color = color)
ax1.scatter(A, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(A,B, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('Google Spend Response Curve vs ROI Curve', fontweight ="bold")
 
# Show plot
plt.show()

########################## Creating Affiliate response/ROI Curve########
input_data_b['roi_affiliate'] = input_data_b['sales'] / input_data_b['affiliate_impressions']

#Creating inputs for plot
A = input_data_b['affiliate_impressions']
Y = input_data_b['sales']
B = input_data_b['roi_affiliate']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('Sales', color = color)
ax1.scatter(A, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(A,B, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('Affiliate Spend Response Curve vs ROI Curve', fontweight ="bold")
 
# Show plot
plt.show()

########################## Creating Paid Spend response/ROI Curve########
input_data_b['roi_paidviews'] = input_data_b['sales'] / input_data_b['paid_views']

#Creating inputs for plot
A = input_data_b['paid_views']
Y = input_data_b['sales']
B = input_data_b['roi_paidviews']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('Sales', color = color)
ax1.scatter(A, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(A,B, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('Paid Views Response Curve vs ROI Curve', fontweight ="bold")
 
# Show plot
plt.show()

#Looking at general time trends - seasonality

###########%% Creating overall impressions plot%%################

#Creating inputs for plot
X = input_data_b['calendar_week']
Y = input_data_b['sales']
Z = input_data_b['roi_overall']



# Creating plot with dataset_1
fig, ax1 = plt.subplots()
 
color = 'tab:red'
ax1.set_ylabel('sales', color = color)
ax1.scatter(X, Y, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
 
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
 
color = 'tab:green'
ax2.set_ylabel('ROI', color = color)
ax2.scatter(X,Z, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
 
# Adding title
plt.title('Sales & ROI overtime', fontweight ="bold")
 
# Show plot
plt.show()

#Plotting using Plotly

import plotly.express as px

fig = px.scatter(input_data_b, x="calendar_week", y="roi_overall") 
#color="species", size='petal_length', hover_data=['petal_width'])
fig.show()



#Plotting ROI overtime omitting low spend weeks
input_data_c = input_data_b.drop(input_data_b.index[0:13], axis=0) #only use inpace=True if you want it to edit the initai dataframe

print(type(input_data_c))
print(type(input_data_b))

fig_b = px.scatter(input_data_c, x="calendar_week", y="roi_overall") 
#color="species", size='petal_length', hover_data=['petal_width'])
fig_b.show()

input_data_c.describe()

fig_c = px.scatter(input_data_c, x="total_impressions", y="roi_overall",
 hover_data=['calendar_week'])
fig_c.show()

fig_d = px.scatter(input_data_c, x="total_impressions", y="sales",
 hover_data=['calendar_week'])
fig_d.show()

#Plotting using Plotly

fig_a = px.scatter(input_data_b, x="calendar_week", y="sales") 
#color="species", size='petal_length', hover_data=['petal_width'])
fig_a.show()

fig_b = px.scatter(input_data_b, x="calendar_week", y="total_impressions") 
#color="species", size='petal_length', hover_data=['petal_width'])
fig_b.show()

ljlksjf
