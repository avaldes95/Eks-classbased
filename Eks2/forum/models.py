from django.db import models
from django.utils.text import slugify

# pip install misaka
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Forum(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='ForumMember')

    def __str__(self):
        return self.name

    def save(self,*arg,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('forum:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']
    pass

class ForumMember(models.Model):
    forum = models.ForeignKey(Forum,related_name='memberships')
    user = models.ForeignKey(User,related_name='user_forums')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('forum', 'user')
