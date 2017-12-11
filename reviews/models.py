import time
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class Product(models.Model):
    name            = models.CharField(max_length=30,unique=True)
    views           = models.IntegerField(default=0)
    details         = models.CharField(max_length=100)
    category        = models.ForeignKey( Category, on_delete=models.CASCADE, blank=True, null = True)
    categorysaver   = models.CharField(max_length=100, null=True, blank=True)
    thumbsUp        = models.IntegerField(default=0)
    thumbsDown      = models.IntegerField(default=0)
    slug            = models.SlugField(blank=True,unique=True)
    comments        = models.IntegerField(default=0)
    pub_date        = models.DateField(auto_now=True, blank=True)
    added           = models.FloatField(default=time.time(), null=True, blank=True)
    image           = models.FileField(upload_to='product-imgs/',null=True, blank=True)
    thumbsUpBy      = models.CharField(max_length=10000, default = "test", null=True, blank=True)
    thumbsDownBy    = models.CharField(max_length=10000, default = "test", null=True, blank=True)
    posted_by       = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class Comment(models.Model):
    title       = models.CharField(max_length=100)
    body        = models.TextField(max_length=200)
    pub_date    = models.DateField(auto_now=True, blank=True)
    added       = models.IntegerField(default=time.time(),  blank=True)
    image       = models.FileField(upload_to='comment-imgs/',null=True, blank=True)
    backs       = models.IntegerField(default=0)
    backedBy    = models.CharField(max_length=10000, default = "test", null=True, blank=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_product_slug = models.CharField(max_length=100, null=True, blank=True)
    posted_by   = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)
# Create your models here.

class UserAccount(models.Model):
    User        = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "user")
    image       = models.FileField(upload_to='profile-imgs/',null=True, blank=True)
    joined      = models.IntegerField(default=time.time(),  blank=True)

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name_plural = 'User Accounts'

class Message(models.Model):
    sent_to        = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "message_to")
    sent_from      = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "message_from")
    body           = models.TextField(max_length=200)
    created        = models.IntegerField(default=time.time(),  blank=True)

    def __str__(self):
        return self.sent_from.username