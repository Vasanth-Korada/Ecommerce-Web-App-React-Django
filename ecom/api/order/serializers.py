from rest_framework import serializers
from .models import OrderModel

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('user','transaction_id','product_names','total_amount','total_products','created_at')
        #TODO: add product and quantity