from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

from item.models import Item

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def daily_sales_plot(request):
    # Query sales data from the database
    items = Item.objects.all().values('created_at', 'price')

    # Convert the query result to a DataFrame
    df = pd.DataFrame(items)

    # Convert 'created_at' column to datetime format
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Set 'created_at' column as the index
    df.set_index('created_at', inplace=True)

    # Resample data to get daily sales
    daily_sales = df.resample('D').sum()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(daily_sales.index, daily_sales['price'], marker='o')
    plt.title('Daily Sales Trends')
    plt.xlabel('Date')
    plt.ylabel('Total Sales (USD)')
    plt.grid(True)

    # Convert plot to image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    buffer_png=base64.b64encode(buffer.getvalue())



    # Close plot
    plt.close()

    # Pass image data to template context
    context = {'image_base64': buffer_png}

    # Render template with image
    return render(request, 'index.html', context)


@login_required
def index(request):
  items=Item.objects.filter(created_by=request.user)
  return render(request,'dashboard/index.html',{
    'items':items,
  })
