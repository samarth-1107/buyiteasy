from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    content1=models.CharField(max_length=5000)
    sub_heading1=models.CharField(max_length=100)
    sub_heading2=models.CharField(max_length=100, default='')
    content2=models.CharField(max_length=5000, default='')
    content3=models.CharField(max_length=5000, default='')
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title