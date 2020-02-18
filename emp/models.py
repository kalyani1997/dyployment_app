from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=50)
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=100)
    econtact=models.CharField(max_length=100)

    class Meta:
        db_table='employee_info'

