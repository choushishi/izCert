from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage #The file storage engine to use when collecting static files with the collectstatic management command.
from django.contrib.staticfiles import finders

# Create your tests here.
class UrlTests(TestCase):
    def test_welcome_page_url(self):
        response = self.client.get(reverse('welcome:index'))
        self.assertEqual(response.status_code, 200)

# Test if static files are served fine
class StaticFileFinderTests(TestCase):

    # Doesn't work - need to come back
    def test_finder_static_files(self):
        staticfiles = [
            'css/bootstrap.min.css',
            'css/sticky-footer.css',
        ]

        for fl in staticfiles:
            self.assertTrue(staticfiles_storage.exists(finders.find(fl)))