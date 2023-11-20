from django.db import models

class Book(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('spanish', 'Spanish'),
        ('french', 'French'),

    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.title