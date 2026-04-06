from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountPagesTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="ali",
            password="StrongPass123!",
            first_name="Ali",
            last_name="Valiyev",
            email="ali@example.com",
            phone_number="+998901234567",
            age=20,
            address="Tashkent",
        )

    def test_edit_page_redirects_when_user_is_not_logged_in(self):
        response = self.client.get(reverse("edit"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_logged_in_user_can_open_edit_page(self):
        self.client.login(username="ali", password="StrongPass123!")
        response = self.client.get(reverse("edit"))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_can_logout_with_post(self):
        self.client.login(username="ali", password="StrongPass123!")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
