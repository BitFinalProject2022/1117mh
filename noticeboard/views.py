import os.path

from django.shortcuts import render
from .models import Notice
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from .models import Post
from .process_image import type_image, do_image


# HttpResponse : Json으로 데이터를 반환(response)하기 위해서 선언
# Create your views here.


# def index(request):
#     article_list = Notice.object.all() # object.all() : table의 모든 값 출력
#     context = {'article_list': article_list}
#
#     return render(request, 'noticeboard/index.html', context)


# json 형태로 파일을 변환하여 저장하는 함수
# def posts(request):
#     #Post 모델(models 안의 값)을 이용하여 데이터를 가여옴
#     posts = Post.objects.filter(published_at__isnull=False).order_by('published_at')
#     post_list = serializers.serialize('json',posts) # 가져온 데이터(QuertSet)을 JSON 타입의 문자열로 반환
#     return HttpResponse(post_list, content_type='text/json-comment-filtered')


def post_detail(request):
    #post = Post.objects.get(pk=pk)
    #json_post = serializers.serialize('json', post)
    print("호호호호")
    data = {'kind': 1, 'qty': 10}
    return JsonResponse(data)


def post_response(response):   # 분석
    path = response.GET['imgUrl']
    print(path)
    file_load = do_image(path)
    print("가나다라마바사아자차카타파하")
    cloth_type = type_image(path)
    print(file_load)
    print(cloth_type)
    data = {'image': file_load, 'small_category': cloth_type[0][0], 'big': cloth_type[1][0], 'qty': cloth_type[0][1]}
    return JsonResponse(data)


#def value(post_response):
