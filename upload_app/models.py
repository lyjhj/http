from __future__ import unicode_literals

from django.db import models
class FileSimpleModel(models.Model):
    file_field = models.FileField(upload_to="upload/%Y/%m/%d")



# Create your models here.
