from django.shortcuts import render, get_object_or_404, redirect
from subscription.models import SubscriptionPlan
from . import models
import requests
from django.http import HttpResponse

def payment_request(request, pk):
    plan = get_object_or_404(SubscriptionPlan, pk=pk)
    
    amount = plan.price
    url = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
    # make a payment record to save details
    payment = models.Payment.objects.create(
        user=request.user, plan=plan, amount=amount)
    headers = {
        "accept": "application/json",
        "content_type": "application/json"
    }
    data = {
        "merchant_id": "755daf07-d29d-40bf-8fe7-3f8e626d9810", #random mercant id
        "amount": amount,
        "description": f"{plan.name}, price: {amount} bought by {request.user}",
        "callback_url": 'http://127.0.0.1:8000/payment/verify/',
    }
    
    # make request
    response = requests.post(url=url, headers=headers, json=data)
    response = response.json()
    if response["data"]["code"] == 100:
        #if successfull save payment authority
        payment.zarinpal_authority = response['data']['authority']
        payment.save()
        return redirect(f"https://sandbox.zarinpal.com/pg/StartPay/{response['data']['authority']}")
    else:
        return HttpResponse(f"Error in payment request: {response['errors']}")
    
    
    
def payment_verify(request):
    """check payment verification."""
    authority = request.GET.get("Authority")
    status = request.GET.get("Status")
    payment = get_object_or_404(models.Payment, zarinpal_authority=authority)
    amount = payment.amount
    url = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
    if status == "OK":
        headers = {
            "accept": "application/json",
            "content_type": "application/json"
        }
        data = { "authority": authority,
                "amount": amount,
                "merchant_id": "755daf07-d29d-40bf-8fe7-3f8e626d9810",
                }
        response = requests.post(url=url, headers=headers, json=data)
        response = response.json()
        if "errors" not in response or len(response["errors"]) == 0:
            response_data = response["data"]
            if response_data["code"] == 100:
                payment.is_paid = True
                payment.zarinpal_ref_id = response_data["ref_id"]
                payment.zarinpal_data = response_data
                payment.save()
                return HttpResponse(""" order payed succesffully
                    thanks for you attention your order will be sent soon
                    """)
            elif response_data["code"] == 101:
                return HttpResponse(
                    """order is repeated order payed successfully 
                    but this order was repeated
                    its saved in the database long time ago""")
            else:
                return HttpResponse("unsuccessfull order")
        else:
            return HttpResponse("unsuccessfull order, error from zarinpal")
                    
    else:
        return HttpResponse("error, status=NOK")
        
