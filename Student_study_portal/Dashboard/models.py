from django.db import models
from django.contrib.auth.models import User


#notes model
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)  # Add this line

    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"

#Assignments
class Assignment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject =models.CharField(max_length=50)
    title= models.CharField(max_length=100)
    description=models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    file_field = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)


    def __str__(self):
        return self.title



#chat


class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return "Room : "+ self.name + " | Id : " + self.slug
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
        # return "Message is : "+ self.content 
        # return "Message is : " + ', '.join([message.content for message in Message.objects.filter(room=self.room)])

        # return " "




class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title


