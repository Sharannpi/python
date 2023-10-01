import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('anime.csv')
print(df)

print(df.info())


#pie
fig = plt.figure(figsize = (10,10))
ax = fig.subplots()
df.type.value_counts().plot(ax=ax, kind='pie')
ax.set_ylabel("Type")
ax.set_title("Modes of watching Anime")
plt.show()

