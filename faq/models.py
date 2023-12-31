

from django.db import models
from autoslug import AutoSlugField

class Terminology(models.Model):
    '''Class used to create the model for the terminology '''
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.CharField(max_length=3000, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__ (self):
        return self.name