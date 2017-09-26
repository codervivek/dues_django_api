from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    date_modified = models.DateTimeField(auto_now=True)

    user_to = models.ForeignKey(User, related_name="borrowers")

    user_from = models.ForeignKey(User, related_name="lenders")
    
    value = models.IntegerField()

    def __str__(self):
        return "%s took %d from %s" % (self.user_to, self.value, self.user_from)

    