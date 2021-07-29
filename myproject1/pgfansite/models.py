from django.db import models
from django.utils import timezone

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    updatedttm = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/', null=True, blank=True) #media/に画像を置く
    username = models.CharField(max_length=20)
    body = models.TextField()
    response_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def body_count(self):
        return len(self.body)

class Response(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    resno = models.IntegerField(default=0)
    published = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=20)
    body = models.TextField()

    #スレッドとレス番号でユニーク制約
    class Meta:
        constraints = [models.UniqueConstraint(fields=['thread', 'resno'], name='unique_stock')]
