from django.db import models
from django.contrib.auth.models import User
# from users.models import Customer

class Tag(models.Model):
    skill = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.skill

#Product
class TutorialList(models.Model):

    DIFFICULTY = (
                ('Beginner', 'Beginner'),
                ('Intermediate', 'Intermediate'),
                ('Advanced', 'Advanced')
    )

    LANGUAGE = (
                ('Korean', 'Korean'),
                ('English', 'English')
    )

    title                         = models.CharField(max_length=150)
    instructor                    = models.CharField(max_length=150)
    link                          = models.URLField(max_length=2000)
    tags                          = models.ManyToManyField(Tag) #skills multi category?
    language                      = models.CharField(max_length=100, choices=LANGUAGE)
    last_updated                  = models.DateField(max_length=100)
    difficulty                    = models.CharField(max_length=100, choices=DIFFICULTY)
    duration                      = models.CharField(max_length=100) #less than 30/ 30-60/ 60 up
    description                   = models.TextField(max_length=2000)

    def __str__(self):
        return self.title + ' | ' + str(self.instructor)

#(name change to customer, stored seperate dir'User' )
class Student(models.Model):
    name                            = models.CharField(max_length=150, null=True)
    email                           = models.CharField(max_length=150, null=True)
    date_created                    = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


#Order: customer can have multiple orders
#Curriculum consists of many tutorials
class Curriculum(models.Model):
    customer                        = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    topic                           = models.CharField(max_length=30, null=True)
    date_created                    = models.DateTimeField(auto_now_add=True, null=True)
    goal                            = models.CharField(max_length=150, null=True)
    note                            = models.CharField(max_length=500, null=True)

    #tutorial                        = models.ForeignKey(TutorialList, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return str(self.customer) + ' | ' + str(self.topic)


# one product goes into order item
# orderitmes will be the items in the cart
#(if physical product, can have multiple quantities but we are digital no quantity needed)

#why seperate? so that curriculum have multiple tutorials?, if I set product into cart, one cart can have only one item.

#orderitem: items in the cart
class CurriculumItem(models.Model):
    tutorial                        = models.ForeignKey(TutorialList, null=True, on_delete= models.SET_NULL)
    curriculum                      = models.ForeignKey(Curriculum, null=True, on_delete= models.SET_NULL)

#OrderItem is connected to Order(curriculum) which is connected to customer.
#Order item model will be connected to the customer with a one to many relationship