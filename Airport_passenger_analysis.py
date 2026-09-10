#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# Data loading
cestujuci = pd.read_csv("Pocet_cestujucich.csv", sep=",")



#Výber stĺpcov z .csv + určenie roku ako indexu 
df_cestujuci = pd.DataFrame(cestujuci, columns=["Rok", "Pravidelná doprava", "Nepravidelná doprava"],)
df_cestujuci.index = df_cestujuci["Rok"]


# Kontrola dát
print(df_cestujuci.info())  #  počet riadkov, stlpce a dat. typy
print(df_cestujuci.describe())  #zákl. štatistiky
print(df_cestujuci.isna().sum()) # kontrola chýbajúcich hodnôt


#Úprava tipu dát na číselný
df_cestujuci["Pravidelná doprava"] = pd.to_numeric(df_cestujuci["Pravidelná doprava"])
df_cestujuci["Nepravidelná doprava"] = pd.to_numeric(df_cestujuci["Nepravidelná doprava"])


#Vytvorenie nového stĺpca "Spolu"
df_cestujuci["Spolu"] = df_cestujuci["Pravidelná doprava"] + df_cestujuci["Nepravidelná doprava"]

del df_cestujuci["Rok"]


# Určeni max a min počet cestujúcich
najviac = df_cestujuci["Spolu"].idxmax()
najmenej = df_cestujuci["Spolu"].idxmin()

print("Najviac cestujúcich bolo v roku:", najviac)
print("Najmenej cestujúcich bolo v roku:", najmenej)

# Určenie rozdielu počtu cestujucich
df_cestujuci["Rozdiel"] = df_cestujuci["Spolu"].diff()

# Určenie rozdielu počtu cestujucich v %
df_cestujuci["Rozdiel_%"] = df_cestujuci["Spolu"].pct_change()

# Určenie roku s najväčším poklesom a nárastom
najvacsi_pokles = df_cestujuci["Rozdiel"].idxmin()
najvacsi_nárast = df_cestujuci["Rozdiel"].idxmax()
print("Najvacsi pokles cestujucich bol v roku :", najvacsi_pokles, ".")
print("Najvacsi nárast cestujucich bol v roku :", najvacsi_nárast, ".")

# Graf vyvoja pravidelnej a nepravidelnej dopravy  
df_cestujuci[["Pravidelná doprava", "Nepravidelná doprava"]].plot(figsize=(16, 8))
plt.xlabel("Roky")
plt.ylabel("Počet cestujucich")
plt.title("Vývoj počtu cestujucich 2008 - 2022")
plt.show()


# Graf medziročnej zmeny počtu cestujucich

df_cestujuci["Rozdiel"].plot(kind="bar",figsize=(16,8))
plt.xlabel("Roky")
plt.ylabel(" Zmena počtu cestujúcich")
plt.title("Medziročná zmena cestujucich")
plt.show()

df_cestujuci.to_csv("Analýza_vývoja_cestujúcich_na_letisku_M.R.Štefánika_2008-2022.csv")


# In[ ]:




