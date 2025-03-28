from django import forms
from .models import Vehicle, Driver, Schedule, Route

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['VIN', 'make', 'model', 'year', 'color','driver', 'status']
        widgets = {
            'VIN': forms.TextInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'license_number', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['start_location', 'end_location', 'distance', 'duration']
        widgets = {
            'start_location': forms.TextInput(attrs={'class': 'form-control'}),
            'end_location': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['vehicle', 'driver', 'route', 'departure_time', 'arrival_time']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'route': forms.Select(attrs={'class': 'form-control'}),
            'departure_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

from django import forms

class JourneyPredictionForm(forms.Form):
    # Numeric inputs remain the same
    distance_km = forms.FloatField(label="Distance (km)")
    temperature = forms.FloatField(label="Temperature (°C)")
    hour_of_day = forms.IntegerField(label="Hour of Day (0-23)")

    # Categorical inputs will be represented as binary encoded variables
    weather_Rainy = forms.BooleanField(label="Rainy Weather", required=False)
    weather_Sunny = forms.BooleanField(label="Sunny Weather", required=False)
    
    traffic_level_Low = forms.BooleanField(label="Low Traffic Level", required=False)
    traffic_level_Medium = forms.BooleanField(label="Medium Traffic Level", required=False)

    day_of_week_Weekend = forms.BooleanField(label="Weekend", required=False)
