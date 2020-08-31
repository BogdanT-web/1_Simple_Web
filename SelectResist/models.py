from django.db import models


class Calc(models.Model):
    title = models.CharField(max_length=200)
    field_1 = models.IntegerField(default=1)
    field_2 = models.IntegerField(default=1)
    field_3 = models.IntegerField(default=1)
    field_4 = models.IntegerField(default=1)
    field_5 = models.IntegerField(default=1)
    field_6 = models.IntegerField(default=1)

    def __str__(self):
        return self.title
