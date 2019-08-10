from django.db import models

# Create your models here.
class Session(models.Model):
    name=models.CharField(max_length=30)
    price_old=models.IntegerField(blank=True)
    price=models.IntegerField()
    photo=models.IntegerField()

    print_small_size=models.CharField(max_length=30)
    print_small=models.IntegerField()

    print_large_size=models.CharField(max_length=30, blank=True, null=True)
    print_large=models.IntegerField(blank=True, null=True)

    print_album=models.IntegerField(blank=True, null=True)

    shooting_time=models.IntegerField('Shooting (Hour)')
    shooting_location=models.IntegerField('Number of Location')

    remark=models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
class Book(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=11)
    date=models.DateField()
    session=models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self):
        return self.name