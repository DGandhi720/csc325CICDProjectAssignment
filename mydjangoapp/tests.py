from django.test import TestCase

from django.urls import reverse


class ViewTests(TestCase):      
	def test_home_page(self):
		response = self.client.get(reverse("home"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.content.decode(),
			"Hello, This is my Django application.",
		)

	def test_about_page(self):
		response = self.client.get(reverse("about"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.content.decode(),
			"This part of the program is my about page.",
		)
	def test_status_page(self):
		response = self.client.get(reverse("status"))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.content.decode(),
			"This is the status page, it shows the status of the application, meaning whether it's running or not.",
		)