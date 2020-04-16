from django.db import models
from .utils import generate_api_key

class App(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    api_key = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.api_key = generate_api_key()
        
        super(App, self).save(*args, **kwargs)

    def update_key(self):
        self.api_key = generate_api_key()
        self.save()
