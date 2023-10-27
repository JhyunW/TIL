from django.db import models


class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품 코드
    kor_co_nm = models.TextField()              # 금융회사 명
    fin_prdt_nm = models.TextField()            # 금융 상품명
    etc_note = models.TextField()               # 상품 설명
    join_deny = models.IntegerField()           # 가입 제한
    join_member = models.TextField()            # 가입 대상
    join_way = models.TextField()               # 가입 방법
    spcl_cnd = models.TextField()               # 우대 조건
    
    
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    intr_rate = models.FloatField(null = True)         # 저축 금리
    intr_rate2 = models.FloatField(null = True)        # 최고 우대 금리
    save_trm = models.IntegerField()        # 저축 기간 / 개월단위