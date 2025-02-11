from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name=models.CharField(max_length=100)
    feature=models.CharField(max_length=120,blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    available=models.BooleanField(default=True)
    image=models.ImageField(blank=True,upload_to="dishes/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    date=models.DateField()
    time=models.TimeField()
    contactname=models.CharField(max_length=100)
    contactsurname=models.CharField(max_length=100)
    guests=models.PositiveIntegerField()
    contactphone=models.CharField(max_length=20)
    comments=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"reservation for {self.contactname} {self.contactsurname} on {self.date} at {self.time}"
    
class Review(models.Model):
    contactname=models.CharField(max_length=100)
    comment=models.TextField(blank=True)
    grades=models.PositiveSmallIntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"rewiev by {self.contactname}"
    








