from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import OrderModel
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({
            "error": "Please Login Again",
            "code": "500"
        })
    if request.method == "POST":
        user_id = id
        transaction_id = request.POST["transaction_id"]
        amount = request.POST["amount"]
        products = request.POST["products"]

        total_pro = len(products.split(',')[:-1])
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({"error": "User Does Not Exist"})

        ordr = OrderModel(user=user, product_names=products, total_products=total_pro,
                          transaction_id=transaction_id, total_amount=amount)
        ordr.save()
        return JsonResponse({"success": True, "error": False, "msg": "Order Placed Successfully"})


@csrf_exempt
def getOrders(request, id):

    if request.method == "GET":
        orders = OrderModel.objects.all().filter(user=id)
        data = serialize("json", orders)
        return JsonResponse({"orders": data})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
