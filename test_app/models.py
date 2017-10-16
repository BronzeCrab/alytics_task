from django.db import models


class DataSet(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)
    exceptions = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    result_calculated_on = models.DateTimeField(null=True, blank=True)
