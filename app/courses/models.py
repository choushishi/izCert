from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe

def course_name_validator(value):
    if not any(c.isalpha() for c in value):
        raise ValidationError(
            _('%(course_name)s contains no alphabetical character'),
            params={'course_name': value}
        )

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200, validators=[course_name_validator])
    course_description = models.CharField(max_length=2000)
    url_name = models.SlugField(max_length=200, editable=False, unique=True)

    def __str__(self):
        return self.course_name
    
    def save(self, *args, **kwargs):
        self.url_name = self.generate_url_name(self.course_name)
        super(Course, self).save(*args, **kwargs)

    @staticmethod
    def generate_url_name(course_name):
        '''
        Generate url name based on course name
        '''
        stack = []
        token = ''
        for c in course_name:
            if c.isalpha():
                token += c
            elif token:
                if len(stack) < 5:
                    stack.append(token)
                    token = ''
                else:
                    return '-'.join(stack)
        if token:
            return '-'.join(stack + [token])
    
    @mark_safe
    def get_url_name(self):
        return self.url_name
    
    def get_template_representation(self):
        return {
            'course_name': self.course_name,
            'course_description': self.course_description,
            'url_name': self.get_url_name(),
        }
