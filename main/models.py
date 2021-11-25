from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    subject = models.CharField(max_length=100, null=False,blank=False)
    body = models.TextField(null=False, blank=False)
    sender_name=models.CharField(max_length=100,null=False,blank=False)
    sender_email = models.EmailField(null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)