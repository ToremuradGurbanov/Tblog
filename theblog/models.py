from django.db import models
from django.contrib.auth.models import User 
import datetime

class ConnectedUser(models.Model):
    choices = (('Technology',('Technology')),('Design', ('Design')),('Business',('Business')),('Science', ('Science')))


    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    person = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='media' , blank = True)
    title = models.CharField(max_length = 100)
    article = models.TextField()
    posted_date = models.DateTimeField(default  = datetime.datetime.now)
    age = models.IntegerField( blank = True)
    application = models.CharField(choices = choices, default = None,   blank = True, max_length = 100)



    def __str__(self):
        return self.firstname + " " + self.lastname

