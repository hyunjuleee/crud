from django.contrib import admin
from .models import Post # .현재 나랑 같은 위치의 models에서 Post 클래스 가져오기
# Register your models here.
admin.site.register(Post)