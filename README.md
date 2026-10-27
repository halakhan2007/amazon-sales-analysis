# Amazon Sales Analysis

## Project Overview

This project explores Amazon sales data using Python to uncover patterns in revenue, customer ratings, regional profitability, and discounting.

Using Pandas for data analysis and Matplotlib for visualization, I investigated business-related questions, compared key metrics, and presented the findings through graphs.

This project helped me practice data cleaning, exploratory data analysis (EDA), data visualization, and interpreting data to generate business insights.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Dataset

The dataset contains Amazon sales information used to explore business performance and customer preferences.

The key attributes include:

- **Product Category:** Categories of products sold.
- **Customer Region:** Geographical regions associated with customers.
- **Payment Method:** Payment methods used for purchases.
- **Discount Percentage:** Discounts applied to products.
- **Revenue:** Revenue generated from sales.
- **Profit:** Profit associated with sales.
- **Rating:** Customer ratings for products.
- **Review Count:** Number of customer reviews.

These attributes were used to investigate revenue patterns, compare customer ratings, analyze regional profitability, and explore the relationship between discounts and revenue.

## Business Questions

1. Which payment method generates the highest revenue?
2. Which product category has the highest average rating?
3. Which customer region generates the highest total profit?
4. Is there any relationship between discount percentage and total revenue?

## Key Findings

- **Revenue by Payment Method:** Wallet was the highest-revenue-generating payment method in the dataset.
- **Customer Ratings:** Books had the highest average customer rating among the product categories analyzed.
- **Regional Profitability:** The Middle East recorded the highest total profit among the customer regions analyzed.
- **Discounts and Revenue:** The analysis found a weak negative correlation between discount percentage and total revenue, suggesting a slight negative association between these variables in the dataset.

## Project Structure

```
amazon-sales-analysis/
|
|- amazon_sales_analysis.py
|
|- amazon_sales.csv
|
|- README.md
|
|_ graphs/
    |
    |- revenue_by_payment_method.png
    |
    |- ratings_by_category.png
    |
    |- profit_by_customer_region.png
    |
    |_ discount_vs_revenue.png

```

## Visualizations

The project includes the following visualizations to communicate the results of the analysis:

- **Revenue by Payment Method:** Compares revenue generated through different payment methods.
- **Average Ratings by Product Category:** Compares average customer ratings across product categories.
- **Profit by Customer Region:** Shows how total profit varies across customer regions.
- **Discount Percentage vs. Revenue:** Uses a scatter plot to explore the relationship between discount percentages and revenue.

## Skills Demonstrated

- Data Cleaning
- Data Exploration
- Data Aggregation using groupby()
- Data Visualization
- Business Insight Generation
- Git & GitHub


## Author

**Hala Khan**

First Data Analysis Project.
