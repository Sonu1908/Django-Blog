from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

    
class Blog(models.Model):
    title=models.CharField(max_length=20)
    blog_image=models.ImageField(upload_to='villen/',null=True,blank=True)
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # status=models.ForeignKey(Section1,on_delete=models.CASCADE)
    date=models.DateTimeField()

    def __str__(self):
        return self.title
    


    