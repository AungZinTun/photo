from django.db import models

# Create your models here.
class Session(models.Model):
    name=models.CharField(max_length=30)
    price_old=models.IntegerField()
    price=models.IntegerField()
    photo=models.IntegerField()

    print_small_size=models.CharField(max_length=30)
    print_small=models.IntegerField()

    print_large_size=models.CharField(max_length=30)
    print_large=models.IntegerField()

    print_a=models.IntegerField()

    shooting_time=models.IntegerField()
    shooting_location=models.IntegerField()

    remark=models.CharField(max_length=100)

    def __str__()
        return self.name