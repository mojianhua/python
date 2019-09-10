from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=32)
    dept = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"

class EmployeeNew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    dept = models.ForeignKey(to="dept",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employeeNew"

class dept(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dept"


class EmployeeNew2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.CharField(max_length=32)
    city = models.ManyToManyField(to="City",through="EmployeeNew2City",through_fields=("EmployeeNew2","City"),related_name="provinceManyToMany")
    dept = models.ForeignKey(to="dept2",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employeeNew2"

class dept2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dept2"

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_cn = models.CharField(max_length=32)
    city_en = models.CharField(max_length=32)

    class Meta:
        db_table = "City"

class EmployeeNew2City(models.Model):
    id = models.AutoField(primary_key=True)
    City = models.ForeignKey(to="City",on_delete=models.CASCADE)
    EmployeeNew2 = models.ForeignKey(to="EmployeeNew2",on_delete=models.CASCADE)

    class Meta:
        db_table = "EmployeeNew2City"