from django.contrib import admin
from .models import Article

# Register your models here.
# models.py에 작성한 파일 등록
admin.site.register(Article) #admin은 관리자 페이지라는 뜻이다.