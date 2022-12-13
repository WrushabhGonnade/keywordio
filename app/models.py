from django.contrib.auth.models import User
from django.db import models



BOOK_CATEGORY = (
    ('Motivational', 'Motivational'),
    ('Biography', 'Biography'),
    ('Autobiography', 'Autobiography'),
    ('Kids', 'Kids'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other')

)
class Book(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    category = models.CharField(choices=BOOK_CATEGORY, max_length=15)
    # Its Demo

    def __str__(self):
        return self.name
