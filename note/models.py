from django.db import models
from user.models import User


# Create your models here.

class Note(models.Model):
    title = models.TextField('标题', max_length=100)
    content = models.TextField('笔记内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField('是否存在', default=True)

    def __str__(self):
        return '笔记' + self.title
