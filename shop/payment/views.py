import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Item


stripe.api_key = settings.STRIPE_PRIVATE_KEY
DOMAIN = settings.DOMAIN


def index(request):
    template = 'payment/index.html'
    return render(request, template)


def item_detail(request, pk):
    template = 'payment/item_detail.html'
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, template, context)


def create_checkout_session(request, pk):
    item = Item.objects.get(pk=pk)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'unit_amount': item.price,
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    }
                },
                'quantity': 1
            },],
            mode='payment',
            success_url=DOMAIN + '/success.html',
            cancel_url=DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e) 
    # return JsonResponse(
    #     {'id': checkout_session.id}
    # )
    return redirect(checkout_session.url, code=303)


def success(request):
    template = 'success.html'
    return render(request, template)


def cancel(request):
    template = 'cancel.html'
    return render(request, template)