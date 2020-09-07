from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=2000)
    url_name = models.CharField(max_length=200, editable=False)

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        self.url_name = self.course_name.replace(' ', '')
        super().save(*args, **kwargs)