from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    created_date = models.DateTimeField('date published')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title