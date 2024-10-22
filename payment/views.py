from django.shortcuts import render, get_object_or_404, redirect
from subscription.models import SubscriptionPlan
import requests
from django.http import HttpResponse


def payment_request(request, pk):
    plan = get_object_or_404(SubscriptionPlan, pk=pk)
    
    amount = plan.price
    url = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
    headers = {
        "accept": "application/json",
        "content_type": "application/json"
    }
    data = {
        "merchant_id": "755daf07-d29d-40bf-8fe7-3f8e626d9810", #random mercant id
        "amount": amount,
        "description": f"{plan.name}, price: {amount} bought by {request.user}",
        "callback_url": 'https://127.0.0.1:8000/payment/verify/',
    }
    
    # make request
    respond = requests.post(url=url, headers=headers, data=data)
    respond = respond.json()
    if respond["data"]["code"] == 100:
        return redirect(f"https://sandbox.zarinpal.com/pg/StartPay/{respond['data']['authority']}")
    else:
        return HttpResponse(f"Error in payment request: {respond['errors']}")
    
