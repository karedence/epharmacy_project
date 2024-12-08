from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Pharmacy, SearchLog
from .forms import PharmacyForm, MedicineForm
from .forms import MedicineSearchForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db import models 




def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})

def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'pharmacy/medicine_form.html', {'form': form})

def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'pharmacy/medicine_form.html', {'form': form})

def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    return redirect('medicine_list')


def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy_list.html', {'pharmacies': pharmacies})

def pharmacy_create(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy_list')
    else:
        form = PharmacyForm()
    return render(request, 'pharmacy/pharmacy_form.html', {'form': form})

def pharmacy_update(request, pk):
    pharmacy = get_object_or_404(Pharmacy, pk=pk)
    if request.method == 'POST':
        form = PharmacyForm(request.POST, instance=pharmacy)
        if form.is_valid():
            form.save()
            return redirect('pharmacy_list')
    else:
        form = PharmacyForm(instance=pharmacy)
    return render(request, 'pharmacy/pharmacy_form.html', {'form': form})

def pharmacy_delete(request, pk):
    pharmacy = get_object_or_404(Pharmacy, pk=pk)
    pharmacy.delete()
    return redirect('pharmacy_list')



def medicine_search(request):
    form = MedicineSearchForm(request.GET or None)
    medicines = []
    pharmacies = []
    
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        medicines = Medicine.objects.filter(name__icontains=search_query)
        pharmacies = Pharmacy.objects.filter(medicines__in=medicines).distinct()

    return render(request, 'pharmacy/medicine_search.html', {'form': form, 'medicines': medicines, 'pharmacies': pharmacies})



def pharmacist_dashboard(request):
    return render(request, 'pharmacy/pharmacist_dashboard.html')


def dashboard(request):
    medicines = Medicine.objects.all()
    total_medicines = medicines.count()
    total_quantity = sum(medicine.quantity for medicine in medicines)
    total_value = sum(medicine.quantity * medicine.price for medicine in medicines)

    context = {
        'total_medicines': total_medicines,
        'total_quantity': total_quantity,
        'total_value': total_value,
    }
    return render(request, 'pharmacy/dashboard.html', context)

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Count
from django.db.models.functions import TruncMonth



# Generate search trend chart
def generate_search_trend_chart():
    # Aggregate search logs by month and medicine
    search_data = (
        SearchLog.objects.annotate(month=TruncMonth('created_at'))  # Group by month
        .values('month', 'medicine__name')
        .annotate(search_count=Count('id'))
        .order_by('month', 'medicine__name')
    )

    # Convert to DataFrame
    df = pd.DataFrame(search_data)
    if df.empty:
        return ""  # Return an empty chart if no data is available

    # Rename columns for readability
    df.rename(columns={'medicine__name': 'medicine', 'month': 'date'}, inplace=True)

    # Group by month and medicine and sum search counts
    aggregated_data = df.groupby(['medicine', 'date'])['search_count'].sum().reset_index()

    # Create a pivot table to structure data for plotting
    pivot_data = aggregated_data.pivot(index='date', columns='medicine', values='search_count')

    # Plotting the data
    plt.figure(figsize=(10, 6))
    pivot_data.plot(kind='bar', stacked=False, figsize=(10, 6))
    plt.xlabel('Month')
    plt.ylabel('Search Count')
    plt.title('Most Searched Medicines by Month')
    plt.xticks(rotation=45)

    # Save the plot to a string buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')


# Predict future orders for all medicines
def predict_future_orders_all():
    # Fetch search logs as a DataFrame
    logs = SearchLog.objects.values('medicine__name', 'created_at')
    df = pd.DataFrame(logs)
    if df.empty:
        return {}

    # Prepare the data
    df['created_at'] = pd.to_datetime(df['created_at']).dt.date
    df = df.groupby(['medicine__name', 'created_at']).size().reset_index(name='search_count')

    predictions = {}
    for medicine_name in df['medicine__name'].unique():
        # Filter data for the current medicine
        medicine_data = df[df['medicine__name'] == medicine_name]
        medicine_data['created_at'] = pd.to_datetime(medicine_data['created_at'])
        medicine_data['days'] = (medicine_data['created_at'] - medicine_data['created_at'].min()).dt.days

        X = medicine_data['days'].values.reshape(-1, 1)
        y = medicine_data['search_count']

        # Train the Linear Regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict future orders for the next 6 months (for example)
        future_days = np.array([max(X) + i for i in range(1, 7)]).reshape(-1, 1)
        future_predictions = model.predict(future_days)

        # Store predictions for the current medicine
        predictions[medicine_name] = list(zip(future_days.flatten(), future_predictions))

    return predictions


# Dashboard view to display analytics
def dashboard(request):
    # Generate the search trend chart
    search_trend_chart = generate_search_trend_chart()

    # Predict future orders for all medicines
    all_predictions = predict_future_orders_all()

    # Get analytics data
    total_medicines = Medicine.objects.count()
    total_searches = SearchLog.objects.count()

    context = {
        'total_medicines': total_medicines,
        'total_searches': total_searches,
        'search_trend_chart': search_trend_chart,
        'predictions': all_predictions,
    }

    return render(request, 'pharmacy/dashboard.html', context)
    
    
  ################Hadoop and Kafka#########################
  
from pyhdfs import HdfsClient
from django.http import JsonResponse
from .models import Medicine

def upload_to_hdfs(request):
    # Connect to HDFS
    hdfs = HdfsClient(hosts='localhost:50070', user_name='hadoop-user')
    data = Medicine.objects.all()
    
    # Create CSV content
    content = "name,quantity,price,description\n"
    for medicine in data:
        content += f"{medicine.name},{medicine.quantity},{medicine.price},{medicine.description}\n"
    
    # Write to HDFS
    hdfs.create('/epharmacy/medicines.csv', content, overwrite=True)
    return JsonResponse({'status': 'Uploaded to HDFS'})  
    
    
 
    
    
    
    
    
    
    
    
    
    
    
