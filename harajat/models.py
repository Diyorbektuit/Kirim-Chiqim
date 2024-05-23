from datetime import date
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from django.db.models import Sum
from django.db.models.functions import TruncHour


class Kirimlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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



#class Products(models.Model):
#    title = models.CharField(max_length=255)
#    created_at = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return self.title
#
#    @classmethod
#    def kunlik_products(cls):
#        today = datetime.now()
#        current_hour = datetime.now().hour
#        start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
#        end_of_day = start_of_day + timedelta(days=1)
#        hourly_counts = cls.objects.filter(created_at__gte=start_of_day, created_at__lt=end_of_day).annotate(
#            hour=TruncHour('created_at')).values('hour').annotate(count=Count('id')).order_by('hour')
#        clock_total = [{'hour': hour_count['hour'].hour, 'count': hour_count['count']} for hour_count in hourly_counts]
#
#        for hour in range(current_hour+1):
#            hour_exists = any(entry['hour'] == hour for entry in clock_total)
#            if not hour_exists:
#                clock_total.append({'hour': hour, 'count': 0})
#
#        clock_total.sort(key=lambda x: x['hour'])
#
#        total_products = sum(entry['count'] for entry in clock_total)
#
#        return {
#            'total_products': total_products,
#            'clock_total': clock_total
#        }
#