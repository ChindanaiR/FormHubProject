from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q, Sum
from form_management.models import Form
from .models import *


def index(request):
    user = request.user

    # Calculate total points
    user_id = request.user.id
    point_plus = PointTransaction.objects.filter(user_id_id = user_id).aggregate(total_points=Sum('point'))['total_points']
    point_negative = RedeemTransaction.objects.filter(user_id_id=user_id).aggregate(total_points=Sum('point'))['total_points']

    if (point_plus):
        point_plus
    else:
        point_plus = 0

    if (point_negative):
        point_negative
    else:
        point_negative = 0

    total_point = (f"{point_plus+point_negative:,}")

    # Ranking
    responses = PointTransaction.objects.filter(user_id = user)
    num_responses = len(responses)

    if num_responses >= 50:
        rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-21-icon.png'
    elif num_responses >= 25:
        rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-Diamond-4-icon.png'
    else:
        rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-Rubin-2-icon.png'

        # # Code below doesnt work since the prizes returns Null so need to do the less efficient way
        # prizes = RedeemTransaction.objects.filter(
        #     Q(redeem__redeem_code = 'PRZ')
        # ).values_list('redeem_id', flat=True)
        # print(prizes)
    
    user_pic = User.objects.get(pk = request.user.id)


    # Show reamining points sum from both form response and redeem

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

    # Form_sale
    form_sale = Form.objects.filter(is_sale=True).exclude(owner=user)
    # print(form_sale)

    return render(request, "redeem/index.html", {
        # "remaining": remaining,
        "cash_options": cash_options,
        "unused_discounts": unused_discounts,
        "unused_prizes": unused_prizes,
        "total_point":total_point,
        "userpic":user_pic.profile_img,
        "form_sale":form_sale,
        "rank": rank
    })

def get_point(request):
    user_id = request.user.id
    point_plus = PointTransaction.objects.filter(user_id_id=user_id).aggregate(total_points=Sum('point'))['total_points']
    point_negative = RedeemTransaction.objects.filter(user_id_id=user_id).aggregate(total_points=Sum('point'))['total_points']

    if (point_plus):
        point_plus
    else:
        point_plus = 0

    if (point_negative):
        point_negative
    else:
        point_negative = 0

    total_point = point_plus+point_negative

    return JsonResponse({'total_point': total_point})

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

def preview_page(request, dataset_id):

    # Get responses
    form = Form.objects.get(pk = dataset_id)
    form_responses = FormResponse.objects.filter(form = form)[:5]
    questions = [section["question"] for section in form.design]

    # Get total points
    user_id = request.user.id
    point_plus = PointTransaction.objects.filter(user_id_id=user_id).aggregate(total_points=Sum('point'))['total_points']
    point_negative = RedeemTransaction.objects.filter(user_id_id=user_id).aggregate(total_points=Sum('point'))['total_points']

    if (point_plus):
        point_plus
    else:
        point_plus = 0

    if (point_negative):
        point_negative
    else:
        point_negative = 0

    total_point = point_plus+point_negative

    return render(request, "redeem/dataset.html", {
        "form_name": form.form_name,
        "questions": questions, 
        "records": form_responses,
        "form": form,
        "user_point": total_point
    })