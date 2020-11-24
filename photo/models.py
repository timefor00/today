from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')

    title = models.CharField(max_length=100, default="제목")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_comments')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ['-id']