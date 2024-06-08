from django.db import models

# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name
    
    
class Student(models.Model):
    
    student_name = models.CharField(max_length=200)
    category_obj=models.ForeignKey(Category,on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
    mobile_number= models.PositiveIntegerField()
    
    def __str__(self):
        return self.student_name
