'''
Created on Feb 4, 2021

@author: maria
'''
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mask = np.array(Image.open('/Users/maria/Document/python/tuxsa//mask/comment.png'))

wine_df = pd.read_csv('/Users/maria/Document/python/tuxsa/csv/winemag-data-130k-v2.csv',
                       index_col=0)
#print(wine_df[['country','points']].head(5))
group_country = wine_df.groupby('country')
#print(group_country.mean().sort_values(by='points', ascending=False))
#print(wine_df.country[1])

text = wine_df.description[1]
print(text)
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1,
                      background_color='white', colormap='Dark2', collocations=False,
                        stopwords = STOPWORDS, mask=mask, contour_width=3, contour_color='teal').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
