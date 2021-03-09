from django.db import models


class Tag(models.Model):
    skill = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.skill


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
    language                      = models.CharField(max_length=100, choices=LANGUAGE) #ko or en
    last_updated                  = models.DateField(max_length=100)
    difficulty                    = models.CharField(max_length=100, choices=DIFFICULTY) #Difficulty: Beginner, Intermediate, Advanced
    estimated_learning_hours      = models.CharField(max_length=100) #less than 30/ 30-60/ 60 up
    description                   = models.TextField(max_length=2000)

    def __str__(self):
        return self.title + ' | ' + str(self.instructor)


class Student(models.Model):
    name                            = models.CharField(max_length=150, null=True)
    email                           = models.CharField(max_length=150, null=True)
    date_created                    = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Curriculum(models.Model):
    student                         = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    tutorial_topic                  = models.CharField(max_length=30, null=True)
    tutorial                        = models.ForeignKey(TutorialList, null=True, on_delete= models.SET_NULL)
    date_created                    = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.student) + ' | ' + str(self.tutorial_topic)
