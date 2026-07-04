import pandas as pd
# load dataset
df = pd.read_csv("netflix_titles.csv")
# show first 5 rows
print(df.head())
# dataset information
print(df.info())
#missing values
print(df.isnull().sum())



#top 10 countries
import matplotlib.pyplot as plt
df['country'].value_counts().head(10).plot(kind='bar', figsize=(10,5))

plt.title("top 10 countries with netflix content")
plt.xlabel("country")
plt.ylabel("count")
plt.tight_layout()
plt.show()

#top 10 ratings
df['rating'].value_counts().head(10).plot(kind='bar', figsize=(10,5))
plt.title("top 10 ratings with netflix ")
plt.xlabel("rating")
plt.ylabel("count")
plt.tight_layout()
plt.show()

print(df.isnull().sum())

print(df.info())

print(df.describe())

#top 10 countries
import matplotlib.pyplot as plt
df['country'].value_counts().head(10).plot(kind='bar', figsize=(10,5))
plt.title("top 10 countries with netflix content")
plt.xlabel("country")
plt.ylabel("count")
plt.tight_layout()
plt.show()

df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6,6)
)

plt.title("movies vs TV shows")
plt.ylabel("")
plt.show()

plt.figure(figsize=(10,5))
df['release_year'].plot(kind='hist', bins=20)

plt.title("distrubution of release years")
plt.xlabel("release year")
plt.ylabel("number of titles")
plt.tight_layout()
plt.show()
