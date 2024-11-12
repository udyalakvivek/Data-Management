from django.db import models

class Student_Data_Model(models.Model):
    name = models.CharField(max_length=50)
    father_name =models.CharField(max_length=60)
    mother_name =models.CharField(max_length=60)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
    
# password = Ak@123 Username = Awnish1    