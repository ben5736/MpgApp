from django.db import models
import datetime

MODEL_YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year + 1)):
    MODEL_YEAR_CHOICES.append((r,r))

class AutoMaker(models.Model):
    name = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length = 30)
    year = models.IntegerField(max_length = 4, choices = MODEL_YEAR_CHOICES, default = datetime.datetime.now().year)
    maker = models.ForeignKey(AutoMaker)

    def __unicode__(self):
        return str(self.year) + " " + str(self.maker) + " " + self.name

class Car(models.Model):
    model = models.ForeignKey(Model)
    owner = models.CharField(max_length = 50)

    def __unicode__(self):
        out = str(self.owner) + "'s"
        out += self.model.__unicode__()
        return out

class Refuel(models.Model):
    gallons = models.DecimalField(max_digits = 8, decimal_places = 4)
    datetime = models.DateTimeField(default = datetime.datetime.now)
    unitprice = models.DecimalField(max_digits = 6, decimal_places = 4)
    miles = models.DecimalField(max_digits = 7, decimal_places = 3)
    car = models.ForeignKey(Car)

    def __unicode__(self):
        out = "Car: " + str(self.car) + " "
        out += "Unit price: " + str(self.unitprice) + " "
        out += "Gallons: " + str(self.gallons) + " "
        out += "Date/Time: " + str(self.datetime)
        return out
