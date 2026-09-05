import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\GAURI RADHIKA\Desktop\PYTHON EXPS\Sales Data.csv")

df['Total_Revenue'] = df['quantity'] *df['unit_price']

print("---SALES DATA---")
print(df)

print("\n--- Sales Summary ---")
total_sales = np.sum(df['Total_Revenue'])
print(f"Total Revenue : Rs.{total_sales:.2f}")

top_product = df.groupby('product_id')['quantity'].sum().idxmax()
print(f"Top Selling Product (by Quantity) : {top_product}")

region_analysis = df.groupby('region')['Total_Revenue'].sum()
print("\n--- Revenue by Region ---")
print(region_analysis)

avg_order = np.mean(df['Total_Revenue'])
print(f"\nAverage Order Value : Rs.{avg_order:.2f}")

print()