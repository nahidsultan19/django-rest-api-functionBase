from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def apiView(request):
    api_list = {
        'List': '/list/',
        'Create': '/create/',
        'Detail': '/detail/<str:pk>/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_list)


@api_view(['GET'])
def List(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detail(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Update(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def Delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response('Successfully Deleted!')
