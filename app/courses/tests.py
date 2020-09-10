from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage #The file storage engine to use when collecting static files with the collectstatic management command.
from django.contrib.staticfiles import finders
from django.conf import settings
from django.db.utils import IntegrityError
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

        cases = {
            '!@#$!@#asdf askdjf-asdf': 'asdf-askdjf-asdf',
            'xxx xx      xx': 'xxx-xx-xx',
            ';lasdmnzxcvh a a a a a a a  a a a a ': 'lasdmnzxcvh-a-a-a-a'
        }

        for name in cases:
            course = Course(course_name=name, course_description='random description')
            course.save()
            saved_course = Course.objects.get(course_name=name)
            self.assertEqual(saved_course.url_name, cases[name])

    def test_course_model_duplication_proof(self):

        existing_course = {
            'course_name': 'a        course with many               spaces',
            'course_description': 'trival'
        }

        new_duplicated_course = {
            'course_name': 'a course with many spaces',
            'course_description': 'trival',
        }

        Course(**existing_course).save()
        self.assertRaises(IntegrityError, Course(**new_duplicated_course).save)
