from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.http import JsonResponse
from django.db.models import Max 

from .serializers import DepositOptionsSerializers, DepositProductsSerializer
from .models import DepositOptions, DepositProducts
import requests


# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    auth = settings.API_KEY
    pageNo = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={auth}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    for li in response.get("result").get("baseList"):
        save_products = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd')
        }
        serializer1 = DepositProductsSerializer(data=save_products)
        if serializer1.is_valid(raise_exception=True):
            serializer1.save()
            
    for li in response.get("result").get("optionList"):
        save_options = {
            'product' : DepositProducts.objects.get(fin_prdt_cd = li.get("fin_prdt_cd")).pk,
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate': li.get('intr_rate'),
            'intr_rate2': li.get('intr_rate2'),
            'save_trm': li.get('save_trm')
        }
        serializer2 = DepositOptionsSerializers(data=save_options)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save()
    return JsonResponse({'message' : 'okay'})
    
    
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # raise_exception=True 설정하면 출력되지 않음
        return Response({'message' : '이미있는 데이터거나, 데이터가 잘못 입력되었습니다'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializers(options, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def top_rate(reqeust):
    get_max = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    options = DepositOptions.objects.get(intr_rate2=get_max['intr_rate2'])
    
    product = DepositProducts.objects.get(fin_prdt_cd=options.fin_prdt_cd)
    
    serializer1 = DepositOptionsSerializers(options)
    serializer2 = DepositProductsSerializer(product)
    
    to_show = {
        'deposit_product':serializer2.data,
        'options':serializer1.data,
    }
    
    return Response(to_show)