from django.shortcuts import render, get_object_or_404
from IPython import embed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def basicinfo(request):
  recipebasic = RecipeBasicInfo.objects.all()
  serializer = RecipeBasicInfoSerializer(recipebasic, many=True)
  # embed()
  return Response(serializer.data)
  
@api_view(['GET'])
def materialinfo(request, basic_pk):
  materials = RecipeMaterialInfo.objects.filter(material_code=basic_pk)
  # for i in materials:
  #   print(i.material_name)

  serializer = RecipeMaterialInfoSerializer(materials, many=True)
  # embed()
  return Response(serializer.data)