from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe

def name_validator(value):
    if not any(c.isalpha() for c in value):
        raise ValidationError(
            _('%(course_name)s contains no alphabetical character'),
            params={'course_name': value}
        )

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

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200, validators=[name_validator])
    course_description = models.CharField(max_length=2000)
    url_name = models.SlugField(max_length=200, editable=False, unique=True)

    def __str__(self):
        return self.course_name
    
    def save(self, *args, **kwargs):
        self.url_name = generate_url_name(self.course_name)
        super(Course, self).save(*args, **kwargs)

    @mark_safe
    def get_url_name(self):
        return self.url_name
    
    def get_template_representation(self):
        return {
            'course_name': self.course_name,
            'course_description': self.course_description,
            'url_name': self.get_url_name(),
        }
    
    def get_sessions(self):
        # Currently only lecture sessions are implmented
        # Add support for other type of sessions in the future
        lectures = self.lecturesession_set.all()
        return sorted(lectures, key=lambda lecture : lecture.order)

class BaseSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=200, validators=[name_validator])
    session_description = models.CharField(max_length=2000)
    session_content = models.CharField(max_length=20000)
    url_name = models.SlugField(max_length=200, editable=False, unique=True)
    order = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.session_name

    def save(self, *args, **kwargs):
        self.url_name = generate_url_name(self.session_name)
        super(BaseSession, self).save(*args, **kwargs)

class LectureSession(BaseSession):
    session_duration = models.DurationField()