from django.db import models

# Create your models here.
class Pred(models.Model):
    PassengerId = models.FloatField(default=0)
    Pclass = models.FloatField(default=0)
    Age = models.FloatField(default=0)
    SibSp = models.FloatField(default=0)
    Parch = models.FloatField(default=0)
    Fare = models.FloatField(default=0)
    C = models.FloatField(default=1)
    S = models.FloatField(default=1)
    Q = models.FloatField(default=1)
    male = models.FloatField(default=0)
    female = models.FloatField(default=0)
    classification = models.CharField(max_length=30)
    def __str__(self):
        return self.classification
    
