from django.test import TestCase
from django.urls import reverse
from .models import OsauhinguAndmedModel

# Create your tests here.
class OsauhinguAndmedTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.OAandmed = OsauhinguAndmedModel.objects.create(
            nimi="Test", registrikood=1001005
        )

    def test_model_content(self):
        self.assertEqual(self.OAandmed.nimi, "Test")
        self.assertEqual(self.OAandmed.registrikood, 1001005)

    def test_home_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "avaleht.html")
        self.assertContains(response, "<h1>Homepage</h1>")
        self.assertContains(response, "Test")

    def test_about_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(response, "<h1>Infot leheküljest</h1>")
