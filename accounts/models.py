from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="profile/pic", blank=True, null=True)
    age = models.PositiveIntegerField()
    phone_regex = RegexValidator(
        regex=r"^\+998\d{9}$",
        message="Telefon raqam faqat +9989XXXXXXXX formatida bolishi lozim!",
    )
    phone_number = models.CharField(
        max_length=15, validators=[phone_regex], unique=True, null=True
    )
    address = models.TextField()
