from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q

from .models import *


def index(request):

    # Calculate total points


    # # Code below doesnt work since the prizes returns Null so need to do the less efficient way
        # prizes = RedeemTransaction.objects.filter(
        #     Q(redeem__redeem_code = 'PRZ')
        # ).values_list('redeem_id', flat=True)
        # print(prizes)

    user = request.user

    # Filter unused redeems
    used_redeems = RedeemTransaction.objects.filter(user_id = user.id).values_list('redeem_id', flat=True)
    unused_redeems = RedeemItem.objects.exclude(id__in = used_redeems)

    # DISCOUNTS
    unused_discounts = unused_redeems.filter(redeem_code = 'DCT')

    # PRIZES
    unused_prizes = unused_redeems.filter(redeem_code = 'PRZ')

    return render(request, "redeem/index.html", {
        "unused_discounts": unused_discounts,
        "unused_prizes": unused_prizes
    })

def redeem(request, redeem_id):
    # This function creates the transaction in RedeemTransaction

    transaction = RedeemTransaction(
        user_id = request.user,
        point = (-1) * RedeemItem.objects.get(id = redeem_id).point,
        redeem = RedeemItem.objects.get(id = redeem_id)
    )
    transaction.save()

    # return JsonResponse({
    #     'alert': 'Conglatulations! You has just successfully redeemed! Enjoy 🥳'
    # })
    return render(request, "redeem/index.html")