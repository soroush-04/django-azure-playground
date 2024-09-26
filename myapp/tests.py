from django.test import TestCase, Client

# Create your tests here.


class GreetingViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greeting(self):
        response = self.client.post("/greeting/", {"name": "Alice"})
        self.assertEqual(response.content.decode(), "Hello, Alice!")

    def test_greeting_no_name(self):
        response = self.client.post("/greeting/", {})
        self.assertEqual(response.content.decode(), "Hello, World!")
