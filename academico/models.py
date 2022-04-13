from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40, null=False)
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}. {self.name} ${self.credits}"
