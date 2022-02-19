
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import productSerializer
from products.models import cover,headset

@api_view(['GET'])
def getcover(request):
    covers=cover.objects.all()
    serializer=productSerializer(covers,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getheadset(request):
    headsets=headset.objects.all()
    serializer=productSerializer(headsets,many=True)
    return Response(serializer.data)