#import the necessary and required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#using pandas, extract the data to be analysed 
df = pd.read_excel('All scraped products.xlsx')

#print the dataset, get the  first few roles, and also what the information contains
print(df.head())
print(df.info())

# keep inspecting the data, the below actually checks the dimensions of the rows and column
print('\nNumber of rows and columns: ', '\n',df.shape)
#print the names of each of the data titles
print('\nColumns names: ', '\n',df.columns)
#check how many null or empty values the data has
print('\nMissing values: ', '\n',df.isnull().sum())

#check the nature of some of these datasets
print(df.dtypes)

#convert the price type to a float value by cleaning each currency symbols
df['price'] = (df['price'].astype(str).str.replace('$', '', regex=False ).str.replace(',', '', regex= False).astype(float))
print(df.dtypes)

#proceeding with the analysis
print('\n price statistics:')
print(df['price'].describe())
print('\nrating statistics:')
print(df['rating'].describe())

# create a histogram to visualize the distribution of product prices    
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='price', bins=20)

plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('number of products')

plt.tight_layout()
plt.savefig('price_distribution.png')
plt.show()

#create a histogram to visualize the distribution of product ratings
sns.histplot(df['rating'],bins=10)

plt.title('Distribution of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Products')

plt.show()

#now continue the analysis and find the top 10 most expensive products
top_10 = df.nlargest(10 , 'price')
print(top_10[['product' , 'price']])
#visualisation
plt.bar(top_10['price'], top_10['product'])
plt.xlabel('Price($)')
plt.ylabel('Products')
plt.title('Top 10 Most Expensive Products')
plt.xticks(rotation=90)
plt.show()

#make a scatter plot to visualize the relationship between price and rating
plt.scatter(df['price'] , df['rating'])

plt.xlabel('price($)')
plt.ylabel('Rating')
plt.title('price vs Rating')
plt.show()

#box plot of price 
plt.boxplot(df['price'])
plt.ylabel('price($)')
plt.title('Price Distribution and Outliers')
plt.show()

#visualize and analyse the rating frequency
rating_counts = df['rating'].value_counts().sort_index()
print(rating_counts)

plt.bar(rating_counts.index,rating_counts.values)

plt.xlabel('Rating')
plt.ylabel('number of products')
plt.title('Number of Products by Rating')
plt.show()