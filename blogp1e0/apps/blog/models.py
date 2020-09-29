from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
#from django.utils.translation import ugettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField(max_length=100, unique=True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()  
    #class Meta:
        # sort comments in chronological order by default
        
    def __str__(self):
        return self.text
