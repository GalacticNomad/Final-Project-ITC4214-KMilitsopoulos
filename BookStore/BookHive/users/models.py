from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # I Create  a one-to-one relationship with the User model
    # If the user is deleted, the associated profile is also delete
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Definining a bio field for the profile, which is a text field
    # The field is optional (blank and null are allowed)    
    bio = models.TextField(blank=True, null=True)

    # Defining an image field for the profile image
    # Images are uploaded to the 'profile_images/' directory
    # The field is optional (blank and null are allowed)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    # I define a boolean field to indicate if the user is a moderator
    # Defaults to False
    is_moderator = models.BooleanField(default=False)
    
    # Baically the string representation of the Profile model
    # Returns the username followed by 'Profile'
    def __str__(self):
        return f'{self.user.username} Profile'


# Registers a signal receiver that listens for the post_save signal from the User model
@receiver(post_save, sender=User)
# this function is to create a Profile instance when a new User is created
# If a new user is created, also create a new profile for the user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Registers another signal receiver that listens for the post_save signal from the User model
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
