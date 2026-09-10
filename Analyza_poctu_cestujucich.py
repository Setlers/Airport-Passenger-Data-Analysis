#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

# Import/načítanie tabuľky, určenie separátora v zdrojovej tabuľke
tabulka = pd.read_csv("cvicne_data.csv", sep=";")

# Vytvorenie dataframe z nančítanej tabuľky, výber stĺpcov ktoré chcem načítať 
df_tabulka = pd.DataFrame(tabulka, columns=["datum", "cena", "mnozstvo"] )
df_tabulka["hodnota"] = df_tabulka["cena"] * df_tabulka["mnozstvo"]

# určenie indexu --> v tomto pripade chcem mať dátum ako index --> bude na osi X
df_tabulka.index = df_tabulka["datum"]


print(df_tabulka)

del df_tabulka["mnozstvo"]
del df_tabulka["hodnota"]

# Vytvorenie grafu z tabuľky, potom zobrazenie vytvoreného grafu, uprava grafu
df_tabulka.plot(figsize=(16,8))
plt.xlabel("Dátum")
plt.ylabel("Cnea")
plt.title("Cena produktov")

plt.show()


# In[ ]:





# In[ ]:




