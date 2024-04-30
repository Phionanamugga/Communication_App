
from django.db import models

# Create your models here.
# a table in a model is considered a class, there create a mode for pupil folder
# you can input all constraints here(model) or you can include it in the views
class Pupil(models.Model): # this will be the main class or table that we are going to use as our database
    first_name = models.CharField("First Name", max_length=50, null =False, blank = False)
    age = models.IntegerField(verbose_name="Age")  # verbose name is used when you want to show something different  # field name and its description  # Field name made lowercase.  
    level = models.CharField(max_length=3)
    last_login = models.DateTimeField("Last Login")  # field name is optional but

    def __str__(self):
    return self.name