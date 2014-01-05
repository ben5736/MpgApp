from django.db import models

class Refuel(models.Model):
    gallons = models.DecimalField(max_digits = 8, decimal_places = 4)
    datetime = models.DateTimeField(auto_now_add=True)
    unitprice = models.DecimalField(max_digits = 6, decimal_places = 4)

    def __unicode__(self):
        out = ""
        out += "Unit price: " + str(self.unitprice) + " "
        out += "Gallons: " + str(self.gallons) + " "
        out += "Date/Time: " + str(self.datetime)
        return out
