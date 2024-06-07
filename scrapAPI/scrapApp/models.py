from django.db import models

# Create your models here.

class MarketDetail(models.Model):
    job_id = models.AutoField(primary_key=True)
    coin_name = models.CharField(default='', max_length=100)
    price = models.CharField(default='', max_length=50)
    data_change = models.CharField(default='', max_length=50)
    market_cap = models.CharField(default='', max_length=50)
    rank_values = models.JSONField(default=list)
    volume = models.CharField(default='', max_length=50)
    vm_ratio = models.CharField(default='', max_length=50)
    circulating_supply = models.CharField(default='', max_length=50)
    total_supply = models.CharField(default='', max_length=50)
    diluted_mc = models.CharField(default='', max_length=50)
    contractor_name = models.CharField(default='', max_length=100)
    contractor_address = models.CharField(default='', max_length=100)
    website = models.URLField(default='')
    social_links = models.JSONField(default=list)