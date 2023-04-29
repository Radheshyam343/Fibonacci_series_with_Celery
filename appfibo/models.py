from django.db import models

class Fibonacci(models.Model):
    n = models.PositiveIntegerField(unique=True)
    value = models.TextField()

    def __str__(self):
        return f"Fibonacci({self.n})"
