from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from .fields import *

# Create your models here.
class Board(models.Model):
    title = models.CharField('Title', max_length=50)
    slug = models.SlugField('Slug', unique=True, allow_unicode=True, help_text='자동으로 기입되니 입력하지 않으셔도 됩니다.', blank=True, null=True)
    content = models.TextField('Content')
    create_date = models.DateTimeField('Create Date', auto_now_add=True, null=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m', null=True, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')
    board_hits = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-modify_date"]

    def __str__(self):
        return self.title

    @property
    def like_count(self):
      return self.like_user_set.count()

    @property
    def update_counter(self):
        self.board_hits = self.board_hits + 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)	
        super(Board, self).save(*args, **kwargs)


    def get_absolute_url(self):
       return reverse("board:detail", args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    board = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
        
