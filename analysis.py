import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/Sample - Superstore.csv', encoding='ISO-8859-1')

# Perform basic analysis
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

# Create visualizations
fig1 = px.bar(sales_by_category, x='Category', y='Sales', title='Sales by Category')
fig2 = px.pie(sales_by_region, names='Region', values='Sales', title='Sales by Region')

# Save visualizations as HTML
fig1.write_html('templates/sales_by_category.html')
fig2.write_html('templates/sales_by_region.html')