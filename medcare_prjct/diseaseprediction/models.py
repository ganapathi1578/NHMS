from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/predicting_cataract/')

    def __str__(self):
        return self.image.name