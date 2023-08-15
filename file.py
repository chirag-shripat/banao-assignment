import unittest
import requests

class WebsiteTest(unittest.TestCase):
    def test_website_loading(self):
        url = 'https://www.youtube.com/'  #URL of the website to test

        # Send a GET request to the website
        response = requests.get(url)

        # Check the status code of the response
        if response.status_code == 200:
            print("Website loaded successfully!")
        else:
            print("Website failed to load!")

        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200, "Website failed to load!")

if __name__ == '__main__':
    unittest.main()
