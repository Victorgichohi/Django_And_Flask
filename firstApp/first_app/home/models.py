from django.db import models

# Create your models here.

class student(models.Model):
      full_name =models.CharField(max_length=200)
      age=models.IntegerField()
      email=models.EmailField()
      interests=models.TextField()
      registered_date=models.DateField(auto_now=False, auto_now_add=True)
      last_update=models.DateField(auto_now=True, auto_now_add=False)

      def _str_(self):
      	 return self.full.full_name
