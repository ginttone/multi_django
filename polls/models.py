from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)#column(변수),datatype
    public_date = models.CharField(max_length=100) #DateTimeField
    votes = models.DecimalField(max_digits=20,decimal_places=10) #BigIntegerField

class Economics(models.Model): # Model상속받아 기능을 향상시킴
    title = models.CharField(max_length=100)#컬럼 이름title은 성격이 str이라
    href = models.CharField(max_length=100) # href성격이 link 고 str이라
    creat_date = models.CharField(max_length=100)#두 날짜 계산해야 할 때 DateTimeField사용