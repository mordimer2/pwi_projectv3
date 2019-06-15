from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)

class Experience(models.Model):
    title = models.CharField(max_length=300)
    subtitle= models.CharField(max_length = 300)
    start_date= models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length = 3000)
    language =models.CharField(max_length = 6)

    def __str__(self):
        return self.title



class Education(models.Model):
    title = models.CharField(max_length=300, null=True)
    school= models.CharField(max_length = 300, null=True)
    start_date= models.DateField(null=True)
    end_date = models.DateField(null=True)
    spec = models.CharField(max_length = 200)
    aver=models.CharField(max_length=4)
    language =models.CharField(max_length = 6)
    
    def __str__(self):
        return self.language + "__" + str(self.title)

class Skills(models.Model):
    skill=models.CharField(max_length=100)

class Workflows(models.Model):
    workflow=models.CharField(max_length=200)
    language =models.CharField(max_length = 6)

    def __str__(self):
        return self.language + "__" + self.workflow

