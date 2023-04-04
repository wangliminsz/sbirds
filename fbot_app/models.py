from django.db import models


class poempoem(models.Model):
    poemid = models.IntegerField()  # 序號
    poemen1 = models.TextField()  # 英文
    poemen2 = models.TextField()  # 英文
    poemen3 = models.TextField()  # 英文
    poemen4 = models.TextField()  # 英文

    poemcn1 = models.TextField()  # 中文
    poemcn2 = models.TextField()  # 中文
    poemcn3 = models.TextField()  # 中文
    poemcn4 = models.TextField()  # 中文

class poem(models.Model):
    poemid = models.IntegerField()  # 序號
    poemen = models.TextField()  # 英文
    poemcn = models.TextField()  # 中文
  
