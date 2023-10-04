from django.db import models

class Dataentries(models.Model):
    dataset_id = models.TextField(blank=True, null=True)
    dataentry_id = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataentries'