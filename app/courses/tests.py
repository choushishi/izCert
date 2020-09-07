from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage #The file storage engine to use when collecting static files with the collectstatic management command.
from django.contrib.staticfiles import finders
from django.conf import settings
import os

from .models import Course

BASE_DIR = settings.BASE_DIR
# Test if static files are served fine
class StaticFileFinderTests(TestCase):

    def test_finder_static_files(self):
        
        static_dir = 'courses/static'

        staticfiles = [
            'courses/style.css',
        ]

        for staticfile in staticfiles:
            css_file_path = os.path.join(BASE_DIR, static_dir, staticfile)
            result = finders.find(staticfile)
            self.assertEqual(result, css_file_path)

class CourseModelTests(TestCase):

    def test_course_model_url_name(self):

        course_names = [
            'a simple test course',
            'some other test courses',
            'some   multiple    spaces',
        ]

        for name in course_names:
            course = Course(course_name=name, course_description='random description')
            course.save()
            saved_course = Course.objects.get(course_name=name)
            self.assertEqual(saved_course.url_name, name.replace(' ', ''))