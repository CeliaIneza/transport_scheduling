from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_type = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    VIN = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    capacity = models.PositiveBigIntegerField(default=5)

    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20,choices=[('Active', 'active'),('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Route(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.FloatField() 
    duration = models.FloatField()  
    estimated_time = models.FloatField(default=0)  # Predicted via ML model

    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location}"


class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    estimated_time = models.FloatField( default= 0)

    def __str__(self):
        return f"Schedule: {self.vehicle} - {self.driver} on {self.route}"
 