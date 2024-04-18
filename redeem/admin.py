from django.contrib import admin

# Register your models here.
from .models import PointTransaction, RedeemItem, RedeemTransaction

admin.site.register(PointTransaction)
admin.site.register(RedeemTransaction)
admin.site.register(RedeemItem)