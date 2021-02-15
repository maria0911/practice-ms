'''
Created on Jan 21, 2021

@author: maria
'''
import pandas as pd
import numpy as np


rates = {'customer_rating': ['Poor', 'fair', 'Excellent']}
df_ordinal = pd.DataFrame(rates)
print(df_ordinal, '\n')

rate_dict = {'Poor':1, 'fair':2, 'Excellent':3}
df_ordinal['customer_rating'] = df_ordinal.customer_rating.map(rate_dict)
print(df_ordinal)

lst = pd.Series([3,5,2], index=[1,2,3])
lst = pd.DataFrame(lst)
print(lst)

#arr_colours = np.array(['green', 'blue', 'orange', 'green', 'blue', 'green' ])
colours = pd.Series(['green', 'blue', 'orange', 'green', 'blue', 'green'], index = [np.array(range(1,7))])
df_colours = pd.DataFrame({'Colours':colours})
print(df_colours)
print('\n')

encode_colours = pd.get_dummies(df_colours,prefix=['favourite_colour'])
print(encode_colours)