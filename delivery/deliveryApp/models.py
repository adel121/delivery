from django.db import models

# Create your models here.

class Manager(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)

class Delivery_Out(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)



class Client(models.Model):
    def __str__(self):
        return self.Company
    Name=models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Company = models.CharField(max_length=50,primary_key=True)

class Delivery_In(models.Model):
    def __str__(self):
        return self.Name
    Name=models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class EndClient(models.Model):
    def __str__(self):
        return self.Name
    Name=models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)

Status_Choices = ( ('paid','PAID'), ('pending','PENDING'), ('sent','SENT'))

class Bill(models.Model):
    def __str__(self):
        return self.Id
    Id = models.CharField(max_length=10, primary_key=True)
    Date = models.DateTimeField('Date')
    address = models.CharField(max_length=100000,default="Address not found")
    delivery_in = models.ForeignKey(Delivery_In, on_delete=models.CASCADE)
    delivery_out = models.ForeignKey(Delivery_Out, on_delete=models.CASCADE)
    end_client = models.ForeignKey(EndClient, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Product_cost = models.DecimalField(max_digits=30, decimal_places=5,default = 0.00)
    Delivery_cost = models.DecimalField(max_digits=30, decimal_places=5, default = 0.00)
    Status = models.CharField(max_length=99, choices=Status_Choices, default="pending" )