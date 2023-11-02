from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name

from tinymce.models import HTMLField
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)    