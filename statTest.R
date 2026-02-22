#Packages
library(data.table)

#Data Loading
pokedex <- fread("pokemon_combined.csv")
pokedex <- data.frame(pokedex)
colnames(pokedex)
typeDamage <- fread("typeDamage.csv")
typeDamage <- data.frame(typeDamage)
print(typeDamage)
typeDamageNumbers <- fread("typeDamageNumbers.csv")
typeDamageNumbers <- data.frame(typeDamageNumbers)
print(typeDamageNumbers)

#Hypothesis 1 Linear Regression Analysis
