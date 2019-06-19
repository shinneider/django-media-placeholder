from django.db import models
from filer.fields.image import FilerImageField, FilerFileField


class SampleModel(models.Model):
    image_field = models.ImageField()
    missing_image_field = models.ImageField()
    file_field = models.FileField()
    filer_image_field = FilerImageField()
    filer_missing_image_field = FilerImageField()
    filer_file_field = FilerFileField()
