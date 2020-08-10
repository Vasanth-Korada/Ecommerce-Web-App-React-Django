from rest_framework import serializers

from .models import CategoryModel

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ("name","description")