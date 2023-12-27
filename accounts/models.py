from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model to store additional user profile information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)  # City associated with the profile
    phone_number = models.CharField(max_length=15)  # Phone number field
    image = models.ImageField(upload_to='profile/')  # Image field for profile pictures
    
    def __str__(self):
        return str(self.user)  # String representation of the profile (user's username)

# Signal receiver: create an empty profile for a new user when created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Create a new empty profile associated with the new user

# Model to represent cities
class City(models.Model):
    name = models.CharField(max_length=30)  # Name of the city
    
    def __str__(self):
        return self.name  # String representation of the city (its name)
