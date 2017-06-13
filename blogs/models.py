from django.db import models

class Category(models.Model):
    title= models.CharField(max_length=120)
    def __str__(self):
        return self.title

    

class Blog(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category)
    Content = models.TextField()
    posted = models.DateField()

    def __str__(self):
        
        return '%s' %(self.title)


