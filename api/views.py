from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializer import AddressSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

address_example_1 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'street': openapi.Schema(type=openapi.TYPE_STRING, example='Vogelpothsweg'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, example='Dortmund'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, example='Germany'),
        'state': openapi.Schema(type=openapi.TYPE_STRING, example='NRW'),
        'postal_code': openapi.Schema(type=openapi.TYPE_INTEGER, example=44227),
    }
)

address_example_2 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'street': openapi.Schema(type=openapi.TYPE_STRING, example='Hohenzollerndamm'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, example='Berlin'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, example='Germany'),
        'state': openapi.Schema(type=openapi.TYPE_STRING, example='BE'),
        'postal_code': openapi.Schema(type=openapi.TYPE_INTEGER, example=10717),
    }
)

@swagger_auto_schema(
    method='post',
    operation_description='This API endpoint creates a new address.',
    request_body=address_example_1,
    responses={201: openapi.Response('New rescource successfully created', AddressSerializer), 400: 'Bad Request'}
)
@api_view(['POST'])
def create_address(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description='This API endpoint returns all the addresses that are stored.',
    responses={200: openapi.Response('Success', AddressSerializer(many=True))}
)
@api_view(['GET'])
def get_addresses(request):
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
        method='get', 
        operation_description="This API endpoint returns the address with the given {id}.", 
        responses={200: openapi.Response('Success', AddressSerializer), 404: 'Address with given {id} does not exist'})
@swagger_auto_schema(
        method='put', 
        operation_description="This API endpoint updates the details of the address with the given {id}.", 
        request_body=address_example_2,
        responses={200: openapi.Response('Success', AddressSerializer), 
                   400: 'Bad Request',
                   404: 'Address with given {id} does not exist'})
@swagger_auto_schema(
        method='delete', 
        operation_description="This API endpoint deletes the address with the given {id}.", 
        responses={204: openapi.Response('HTTP Request successfully completed (Returns no content)', AddressSerializer), 
                   404: 'Address with given {id} does not exist'})
@api_view(['GET', 'PUT', 'DELETE'])
def address_detail(request, pk):
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


