from django.db import models
from django.utils.safestring import mark_safe

# Create your models he
class Album (models.Model):
    cat=[('P', 'Portrait'), ('G', 'Graduation'), ('W', 'Prewedding'), ('F', 'Family'), ('B', 'Baby'), ('C', 'Ceremony'), ('D', 'Product')]
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    category=models.CharField(max_length=1, choices=cat, default='Portrait')
    def __str__(self):
        return self.name

class Photo(models.Model):
    photo=models.ImageField(upload_to='static/img/portfolio')
    album=models.ForeignKey(Album, on_delete=models.CASCADE )
    lighting=models.CharField(max_length=1, choices=(('u' , 'Under'), ('n', 'normal'), ('o' , 'over')) )
    situation=models.CharField(max_length=1, choices=(('u' , 'Under'), ('n', 'normal'), ('o' , 'over')) )
    mood=models.CharField(max_length=1, choices=(('u' , 'Under'), ('n', 'normal'), ('o' , 'over')) )
    fov=models.CharField(max_length=1, choices=(('s' , 'Wide'), ('n', 'normal'), ('t' , 'tele')) )
    def __str__(self):
        return mark_safe('<img src="/%s" width="200" height="200"/>' % (self.photo))
    def image_tag(self):
        return mark_safe('<img src="/%s" width="200" />' % (self.photo))
      
      
        
      

  