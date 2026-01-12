from django.db import models


class InputForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.IntegerField(help_text="Enter 6 digit roll number")
    password = models.CharField()
    photos=models.ImageField(upload_to='media/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name