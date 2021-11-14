from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, default=None, null=True)
    type = models.CharField(max_length=100, default=None, null=True)
    avatar = models.ImageField(default='avatars/default.jpg', upload_to='avatars/')
    cover = models.ImageField(default='avatars/covers/default.jpg', upload_to='avatars/covers/')

    def __str__(self):
        return f'{self.user.first_name}\'s profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
