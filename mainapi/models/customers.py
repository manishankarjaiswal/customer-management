from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Custom validator for Indian phone numbers
def validate_phone_number(value):
    phone_regex = RegexValidator(regex=r'^[1-9][0-9]{9}$', message="Phone number must be a valid Indian mobile number with 10 digits long.")
    phone_regex(value)  # This will raise a ValidationError if the number is invalid


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10, validators=[validate_phone_number])
    address = models.TextField()

    class Meta:
        unique_together = ('user', 'phone_number')
        indexes = [
            # Composite index on 'first_name' and 'last_name'
            models.Index(fields=['first_name', 'last_name'], name='first_last_name_idx'),
            models.Index(fields=['address'])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
