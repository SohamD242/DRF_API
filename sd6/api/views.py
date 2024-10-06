from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

#@api_view() -> default GET 
@api_view(['GET', 'POST'])
def api_fun(request):
    if request.method == 'GET':
        return Response({'msg':'This is GET Response'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is POST Response'})
