# analytics.py
import os
import django
from django.conf import settings
import pandas as pd
import matplotlib.pyplot as plt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')  
django.setup()


from item.models import Item

# Assuming Item has a field called 'created_at' representing the date the item was created/sold
items = Item.objects.all().values('created_at', 'price')
df = pd.DataFrame(items)
df['created_at'] = pd.to_datetime(df['created_at'])
df.set_index('created_at', inplace=True)
daily_sales = df.resample('D').sum()  # Resample daily instead of monthly

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales['price'], marker='o')
plt.title('Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Total Sales (USD)')
plt.grid(True)
plt.show()

