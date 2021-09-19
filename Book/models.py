from django.db import models
from django.db.models.manager import Manager


# Create your models here.

class ActiveBooksManager(models.Manager):                  # Custom manager instead of objects.all() to get Active books
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = 'N')

class InactiveBooksManager(models.Manager):               # Custom manager instead of objects.all() to get Inactive books
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = 'Y')

class Book(models.Model):
    """ This class contails book details"""
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length=1 , default="N")
    active_books = ActiveBooksManager()
    inactive_books = InactiveBooksManager()
    all_books = Manager()

    def __str__(self):
        return f"{self.__dict__}"

    class Mata:
        db_table = "book"


