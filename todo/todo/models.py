from django.db import models ##provides db models reprents db tables and theirs relationship
from django.contrib.auth.models import User ##imports djang0 authentication framework

class TODOO(models.Model):
    srno =models.AutoField(primary_key=True, auto_created=True)
    ## Each TODOO entry will have a unique serial number (like 1, 2, 3...).
    title = models.CharField(max_length=25)
    # A short text field for the title of the task
    # max_length=25: Limits it to 25 characters.
    date = models.DateTimeField(auto_now_add=True)
    # Stores the timestamp when the object is created.
    # auto_now_add=True: Automatically fills the field with the current date & time on object creation.
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    # Links each TODOO to a specific user (from Django's auth.User model).
    # ForeignKey: Creates a relationship (many TODOOs to one User).
    # on_delete=models.CASCADE: If a user is deleted, all their TODOOs are also deleted.