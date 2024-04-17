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

    # Show reamining points sum from both form response and redeem
    points_formresponse = FormResponse.objects.filter(responder = user)
    points_redeem = RedeemTransaction.objects.filter(user_id = user)

    # create new field to store points in FormResponse
    # remaining = sum(points_formresponse) + sum(points_redeem.point)

    # CASH
    cash_options = RedeemItem.objects.filter(redeem_code = 'CSH')

    # Filter unused redeems
    used_redeems = RedeemTransaction.objects.filter(user_id = user.id).values_list('redeem_id', flat=True)
    unused_redeems = RedeemItem.objects.exclude(id__in = used_redeems)

    # DISCOUNTS
    unused_discounts = unused_redeems.filter(redeem_code = 'DCT')

    # PRIZES
    unused_prizes = unused_redeems.filter(redeem_code = 'PRZ')

    return render(request, "redeem/index.html", {
        # "remaining": remaining,
        "cash_options": cash_options,
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


    print(f"{request.user} Redeem {RedeemItem.objects.get(id = redeem_id).description}")
    
    return JsonResponse({
        'alert': 'Conglatulations! You has just successfully redeemed! Enjoy 🥳'
    })

    # return HttpResponseRedirect(reverse("index"))
