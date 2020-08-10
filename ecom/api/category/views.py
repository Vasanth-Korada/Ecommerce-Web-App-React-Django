from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import CategoryModel

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all().order_by('name')
    serializer_class = CategorySerializer