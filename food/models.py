from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length = 200)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default = "https://th.bing.com/th/id/OIP.LWunzgdDcx2JtgDBYntqggHaFj?rs=1&pid=ImgDetMain")