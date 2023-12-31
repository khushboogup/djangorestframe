from rest_framework.response import  Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializer import ItemSerializer
@api_view(['GET'])
def getData(request):
    item=Item.objects.all()
    serializer=ItemSerializer(item,many=True)
    # person={'name':'khushboo','age':'23'}
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
