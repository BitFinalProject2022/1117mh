from django.db import models
from django.utils import timezone

# Create your models here.


# mysql DB에 해당 컬럼으로 된 파일 생성
# makemigrations > migrate 순서대로 입력 후 runsever 실
class Notice(models.Model):
    test_id = models.IntegerField()
    test_name = models.CharField(max_length=30)
    test_type = models.CharField(max_length=30)
    test_created = models.DateTimeField(timezone.now(), editable=False)
    test_image = models.ImageField(upload_to='noticeboard/image/%Y/%M/%D', blank=True)

    def __str__(self): # test_name 리턴인데 모르겠습니다.
        return self.test_name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title