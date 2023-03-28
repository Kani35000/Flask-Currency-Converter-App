from unittest import TestCase  

from app import app 

class ConverterTestCase(TestCase):
    """Tests for views about desserts."""

    def Convert_homepage_test(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button class="btn btn-success" type="submit">See Conversion</button>')
            self.assertEqual(convert())