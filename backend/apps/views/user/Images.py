from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *

image_url = 'http://127.0.0.1:8081/'


class UploadImage(APIView):
    def post(self, request):
        file_obj = request.FILES.get('img')
        img = Image.objects.create(
            img=file_obj
        )
        img.save()
        return Response({'reason': '上传成功',
                         "url": image_url + img.img.url, "id": img.id}, status=200)


class GetImageUrl(APIView):
    def get(self, request):
        image_id = request.GET['img_id']
        img = Image.objects.get(
            id=image_id
        )
        return Response({'reason': "获取成功", 'url': image_url + img.img.url}, status=200)
