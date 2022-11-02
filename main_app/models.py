from django.db import models

class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.quantity} {self.description}s"