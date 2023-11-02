from djongo import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
