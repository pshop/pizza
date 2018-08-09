from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostalAddress(models.Model):

    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300, blank=True)
    postal_code = models.CharField(max_length=5)
    town = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserInfo(models.Model):
# A user has:
    # username (defined in User)
    # first_name (defined in User)
    # last_name (defined in User)
    # email (defined in User)
    # password (deinied in User)
    # phone_number
    # user_type
    # user_address (defined in PostalAddress)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)






