import pandas as pd
import matplotlib.pyplot as plt

#reading dataset
df=pd.read_csv("amazon_sales.csv")

#setting option to display all columns
pd.set_option('display.max_columns', None)

#Retrieving basic info
print("\n", "="*10, "First five rows of the dataset", "="*10)
print(df.head())
print("\n","="*10, "Last five rows of the dataset", "="*10)
print(df.tail())
print("\n","="*10, "Shape of the dataset", "="*10)
print(df.shape)
print("\n","="*10, "Names of the columns of the dataset", "="*10)
print(df.columns)

#checking data quality
print("\n","="*10, "Information about the dataset", "="*10)
df.info()
print("\n","="*10, "Number of Null values in the dataset", "="*10)
print( df.isnull().sum())
print("\n","Number of duplicated values:", df.duplicated().sum())

#statistical summary
print("\n","="*10, "Statistical Summary of the dataset", "="*10)
print(df.describe())

#Which payment method generates the highest revenue?
print("\n","="*10, "Business Question 1", "="*10)
payment_revenue=df.groupby("payment_method") ["total_revenue"].sum()
print("Payment method with highest revenue:", payment_revenue.idxmax())
print("Highest revenue:", payment_revenue.max())

# Visualisation for Business Question 1
plt.figure(figsize=(8,5))

plt.bar(payment_revenue.index, payment_revenue.values)
plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")

plt.savefig("graphs/revenue_by_payment_method.png", dpi=300)
plt.show()

#Which category has the highest average rating?
print("\n","="*10, "Business Question 2", "="*10)
category_rate=df.groupby("product_category")["rating"].mean()
print("Category with the highest average rating:", category_rate.idxmax())
print("Highest average rating:", category_rate.max())

# Visualisation for Business Question 2
plt.figure(figsize=(8,5))
plt.bar(category_rate.index, category_rate.values)
plt.title("Ratings by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Rating")

plt.tight_layout()
plt.savefig("graphs/ratings_by_category.png", dpi=300)
plt.show()

#Which customer region generates the highest total profit?
print("\n","="*10, "Business Question 3", "="*10)
region_profit=df.groupby("customer_region")["profit"].sum()
print("Customer region with highest total profit:", region_profit.idxmax())
print("Highest total profit:", region_profit.max())

# Visualisation of Business Question 3
plt.figure(figsize=(8,5))

plt.bar(region_profit.index, region_profit.values)
plt.title("Profit by Customer Region")
plt.xlabel("Customer Region")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("graphs/profit_by_customer_region.png", dpi=300)
plt.show()

#Checking the correlation between discount_percent and total_revenue
discount_revenue=df[['discount_percent','total_revenue']].corr()
print("\n","="*10, "Correlation Matrix", "="*10)
print(discount_revenue)

#Creating a scatter plot to visually check the correlation
plt.figure(figsize=(8,5))

plt.scatter(df['discount_percent'], df['total_revenue'],
            s=5,
            alpha=0.2
            )
plt.title("Relationship Between Discount Percentage and Total Revenue")
plt.xlabel("Discount Percentage")
plt.ylabel("Total Revenue")
plt.savefig("graphs/discount_vs_revenue.png", dpi=300)
plt.show()

#Checking number of orders on each discount rate for cross checking the graph
print("\n"*2)
print(df["discount_percent"].value_counts())
