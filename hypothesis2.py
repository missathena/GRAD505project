#Packages Needed
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols

#Data loading
pokedex = DataFrame(pd.read_csv('pokemon_combined.csv'))
pokedex = pokedex[pokedex.groupby('Type')['Type'].transform('count') >= 5]
pokedex = DataFrame.drop(pokedex,columns=["Abilities","Growth Rate"])
typeDamageNumbers = DataFrame(pd.read_csv('typeDamageNumbers.csv'))
print(typeDamageNumbers.head())
print(pokedex.head())

#Hypothesis 2 Linear Regression
kg_atk_def = DataFrame(pd.read_csv('weight_attack_defense.csv'))

kg_atk =  DataFrame(kg_atk_def[['Weight','Attack']])
kg_def = DataFrame(kg_atk_def[['Weight','Defense']])


model1 = ols('Attack ~ Weight',data=kg_atk).fit()
print(model1.summary())
model2 = ols('Defense ~ Weight',data=kg_def).fit()
print(model2.summary())

plot1 = sns.regplot(data=kg_atk,x='Weight',y='Attack')
plt.title('Attack Power and Weight Regression Plot')
plt.show()

plot2 = sns.regplot(data=kg_def,x='Weight',y='Defense')
plt.title('Defense Level and Weight Regression Plot')
plt.show()

sns.residplot(data=kg_def,x='Weight',y='Defense')
plt.title('Defense Level and Weight Residual Plot')
plt.show()

sns.residplot(data=kg_atk,x='Weight',y='Attack')
plt.title('Attack Power and Weight Residual Plot')
plt.show()





