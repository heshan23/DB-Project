from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class AddNewTag(APIView):
    def post(self, request):
        try:
            name = request.data['tag_name']
        except KeyError:
            return Response({"reason": "数据格式有误"}, status=422)
        tag = Tag.objects.create(
            name=name
        )
        tag.save()
        return Response({"reason": "", "tag_id": tag.id}, status=200)


class GetAllTag(APIView):
    def get(self, request):
        ret_data = []
        for tag in Tag.objects.filter():
            ret_data.append(tag.name)
        return Response({"reason": "", "data": ret_data}, status=200)