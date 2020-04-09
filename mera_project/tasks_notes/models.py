from django.db import models
from django.contrib.auth.models import User

class BudgetInfo(models.Model):
    item= models.CharField(max_length=20)
    cost= models.FloatField(blank=False, null=True)
    date_added= models.DateField()
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
    	return str(self.user)
