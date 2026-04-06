from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "email",
            "phone_number",
            "age",
            "avatar",
            "address",
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not username:
            raise ValidationError("Username bosh bolishi mumkin emas!")

        username = username.strip()

        if not re.fullmatch(r"^[a-zA-Z0-9_-]+$", username):
            raise ValidationError(
                "Username faqat harflar, raqamlar, '-' va '_' belgilardan iborat bolishi kerak!"
            )

        if len(username) < 3:
            raise ValidationError("Username kamida 3 ta belgidan iborat bolishi kerak!")

        if len(username) > 30:
            raise ValidationError("Username maksimal 30 belgidan oshmasligi kerak!")

        if username.objects.filter(username=username).exists():
            raise ValidationError("Bu username allaqachon ishlatilgan!")

        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise ValidationError("Ism bosh bolishi mumkin emas!")
        first_name = first_name.strip()
        if not re.fullmatch(r"^[a-zA-Zа-яА-ЯёЁ\-']+$", first_name):
            raise ValidationError("Ismda faqat harflar bo'lishi kerak!")
        if len(first_name) < 2:
            raise ValidationError("Ism kamida 2 ta harfdan iborat bo'lishi kerak!")
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise ValidationError("Familya bosh bo'lishi mumkin emas!")
        last_name = last_name.strip()
        if not re.fullmatch(r"^[a-zA-Zа-яА-ЯёЁ\-']+$", last_name):
            raise ValidationError("Familyada faqat harflar bo'lishi kerak!")
        if len(last_name) < 3:
            raise ValidationError("Familya kamida 3 ta harfdan iborat bo'lishi kerak!")
        return last_name.capitalize()

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age is None:
            raise ValidationError("Yosh kiritilishi shart!")
        if not (0 <= age <= 120):
            raise ValidationError("Iltimos, togri yosh kiriting!")
        if age < 18:
            raise ValidationError("18 yoshdan kichkinalar kirish mumkin emas!")
        return age

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            pctr = avatar.content_type
            if pctr not in ["image/jpeg", "image/png"]:
                raise ValidationError("Shu file typelar qabul qilinadi: JPEG yoki PNG")
        return avatar

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if not address:
            raise ValidationError("Manzil kiritilishi shart!")
        if address.strip().lower() != "tashkent":
            raise ValidationError("Faqat Tashkent manzili qabul qilinadi!")
        return address


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ["last_name", "first_name", "address"]
