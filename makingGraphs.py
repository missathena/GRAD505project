import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pokedex = pd.DataFrame(pd.read_csv("pokemon_combined.csv"))
typeDamage = pd.DataFrame(pd.read_csv("typeDamage.csv"))
