from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=30, help_text='Enter the driver\'s first name')
    last_name = models.CharField(max_length=30, help_text='Enter the driver\'s last name')
    email = models.EmailField(max_length=100, unique=True, help_text='Enter the driver\'s email address')
    phone_number = models.CharField(max_length=20, help_text='Enter the driver\'s phone number')
    license_number = models.CharField(max_length=20, help_text='Enter the driver\'s license number')
    address = models.CharField(max_length=100, help_text='Enter the driver\'s address')
    birth_date = models.DateField(null=True, blank=True, help_text='Enter the driver\'s date of birth (optional)')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.last_name}, {self.first_name}'


class Vehicle(models.Model):
    """Model to represent a vehicle."""

    # Vehicle identification number (VIN)
    vin = models.CharField(max_length=17, unique=True, help_text='Enter the VIN of the vehicle.')

    # Make and model of the vehicle
    make = models.CharField(max_length=30, help_text='Enter the make of the vehicle.')
    model = models.CharField(max_length=30, help_text='Enter the model of the vehicle.')

    # Year the vehicle was manufactured
    year = models.PositiveIntegerField(help_text='Enter the year the vehicle was manufactured.')

    # License plate number of the vehicle
    license_plate = models.CharField(max_length=10, help_text='Enter the license plate number of the vehicle.')

    # Color of the vehicle
    color = models.CharField(max_length=30, help_text='Enter the color of the vehicle.')

    # Date and time the vehicle was added to the database
    date_added = models.DateTimeField(auto_now_add=True,
                                      help_text='Date and time the vehicle was added to the database.')

    def __str__(self):
        """String representation of the Vehicle model."""
        return f'{self.make} {self.model} ({self.year})'


class Trip(models.Model):
    """Model to represent a trip."""

    # Primary key for the trip
    trip_id = models.AutoField(primary_key=True, help_text='Primary key for the trip.')

    # Foreign key to the Vehicle model
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, help_text='Foreign key to the Vehicle model.')

    # Foreign key to the Driver model
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, help_text='Foreign key to the Driver model.')

    # Other fields for the trip
    # ...

    def __str__(self):
        """String representation of the Trip model."""
        return f'Trip {self.trip_id}'


class Location(models.Model):
    # trip = models.ForeignKey(Trip, on_delete=models.CASCADE, default=1)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    altitude = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    speed = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    vsat = models.IntegerField(default=0)
    usat = models.IntegerField(default=0)
    accuracy = models.DecimalField(max_digits=9, decimal_places=2, default=1)  # Agrega un valor predeterminado
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    uid = models.CharField(max_length=100, default="123")

    # def __str__(self):
    #     return f"Point({self.latitude}, {self.longitude}, {self.altitude}) - Trip ID: {self.trip_id}"
