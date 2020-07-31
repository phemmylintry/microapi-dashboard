from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_id = models.CharField(_("Id sent from auth api"), max_length=255)
    is_company = models.BooleanField(default=False)
    