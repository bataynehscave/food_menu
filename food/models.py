from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.name

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length = 200)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default = "https://th.bing.com/th/id/OIP.LWunzgdDcx2JtgDBYntqggHaFj?rs=1&pid=ImgDetMain")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('food:item-details', kwargs={'pk': self.pk})