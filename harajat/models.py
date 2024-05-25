from datetime import date
from users.models import TgUsers
from django.db import models
from django.db.models import Sum



class Kirimlar(models.Model):
    user = models.ForeignKey(TgUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    cost = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def kunlik_kirimlar(cls):
        today = date.today()
        return cls.objects.filter(date=today)
    
    @classmethod
    def kunlik_kirimlar_umumiy(cls):
        today = date.today()
        result = cls.objects.filter(date=today).aggregate(total_cost=Sum('cost'))
        return result['total_cost']

    @classmethod
    def oylik_kirimlar(cls):
        today = date.today()
        month = today.month
        result = cls.objects.filter(date__month=month)
        return result

    @classmethod
    def oylik_kirimlar_umumiy(cls):
        today = date.today()
        month = today.month
        result = cls.objects.filter(date__month=month).aggregate(total_cost=Sum('cost'))
        return result['total_cost']


class Chiqimlar(models.Model):
    user = models.ForeignKey(TgUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    cost = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def kunlik_chiqimlar(cls):
        today = date.today()
        return cls.objects.filter(date=today)

    @classmethod
    def kunlik_chiqimlar_umumiy(cls):
        today = date.today()
        result = cls.objects.filter(date=today).aggregate(total_cost=Sum('cost'))
        return result['total_cost']

    @classmethod
    def oylik_chiqimalar(cls):
        today = date.today()
        month = today.month
        result = cls.objects.filter(date__month=month)
        return result

    @classmethod
    def oylik_chiqimlar_umumiy(cls):
        today = date.today()
        month = today.month
        result = cls.objects.filter(date__month=month).aggregate(total_cost=Sum('cost'))
        return result['total_cost']

