from django.db import models
from django.urls import reverse

class Bookmark(models.Model) :
    # 모델은 생성 및 수정 후 반드시 마이그레이션을(테이블생성) 해 주어야 한다.
    # 필드타입이 결정하는 것들: 컬럼타입 및 제약사항, form 타입 및 제약사항
    site_name = models.CharField(max_length=100)   # 100글자
    url = models.URLField('Site URL')      # 자동링크 타입, 'Site URL' 이란 레이블로 설정

    def __str__(self):
        return f'이름 : {self.site_name}, 주소: {self.url}'

    def get_absolute_url(self) :   # 장고에서 제공하는 [성공처리 후 이동경로 설정]하는 메소드
        # return reverse('detail', args=[self.id])
        return reverse('list')