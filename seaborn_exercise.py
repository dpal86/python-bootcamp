import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips') 

print(tips.dtypes)
print(tips.describe())
print(tips.head(10))

sns.set_style('whitegrid', {'grid.linestyle': '--',
                             'grid.color': '.8',
                             'axes.edgecolor': '0.2',
                             'xtick.color': '0.3',
                             'ytick.color': '0.3'})

sns.set_context('talk')
sns.set_palette('colorblind')

sns.set_theme(style='whitegrid', context='talk', palette='deep',
             font='Calibri', font_scale=1.1,
             rc={'figure.figsize': (10, 6), 'axes.titlesize': 16})



sns.scatterplot(x='total_bill', y='tip', data=tips)
sns.boxplot(x='day', y='total_bill', hue='smoker',data=tips)
plt.show()

sns.barplot(x='day', y='total_bill', data=tips)

plt.show()

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="smoker")
plt.show()
