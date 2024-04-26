
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# In[2]:


df = pd.read_csv("Data_Orders.csv")

st.write(df.head())



# ## Orders by Category

Categories = df['Category'].value_counts()

# matplotlib
#st.header("Matplotlib")
#st.subheader("Line Plot")
fig = plt.figure(figsize=(15,8))
plt.plot(Categories, 'bo--',c='b',lw=3, marker ='.',markersize =15,ls='--')
plt.title('Orders by Category', fontsize=15)
plt.xlabel('Categort')
plt.ylabel('Orders')
st.pyplot(fig)



# ## Orders by Country

country_orders = df['Country'].value_counts()

fig = plt.figure(figsize=(15,8))

plt.bar(country_orders.index, country_orders.values)
#plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Orders')
plt.grid(axis='y', color='g', alpha=0.35, linestyle=':')
plt.title('Orders by Country', fontsize=15)
plt.xlabel('Country')
plt.ylabel('Orders')
st.pyplot(fig)


# ## Orders by Status

status = df['Status'].value_counts()
fig = plt.figure(figsize=(15,8))


mylabels = status.values / status.values.sum()*100
plt.pie(status, startangle=90, labels=mylabels.round(1), colors=['#2D3250', '#F6B17A'], shadow=False)
plt.legend(labels=status.index, loc='upper right')
st.pyplot(fig)


# ## Quantity and Total Cost by Category



Cat_Quan_TotCost = df.groupby('Category')[['Quantity', 'Total Cost']].sum()


fig, axis = plt.subplots(nrows=2, ncols=1)
#fig.suptitle('Main Title')
fig.patch.set_facecolor('#e6e6e6')
fig.subplots_adjust(hspace=0.5)

axis[0].plot(Cat_Quan_TotCost['Quantity'], 'r')
axis[0].set_xticks([])
axis[0].set_title('Quantity by Category')

axis[1].plot(Cat_Quan_TotCost['Total Cost'])
axis[1].tick_params(axis='x', rotation=45)
axis[1].set_title('Cost by Category')
st.pyplot(fig)