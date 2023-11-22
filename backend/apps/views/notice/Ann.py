from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class AddAnn(APIView):
    def post(self, request):
        try:
            content = request.data['content']
        except KeyError:
            return Response({"reason": "公告未传递内容"}, status=422)
        ann = Ann.objects.create(
            content=content,
            create_date=timezone.now()
        )
        ann.save()
        return Response({"reason": "公告发布成功"}, status=200)


class GetNowNotice(APIView):
    def get(self, request):
        try:
            # 这个user是接受信息的人
            user_id = request.GET['user_id']
        except KeyError:
            return Response({"reason": "检查数据是否给出userid"}, status=422)
        notices = Notice.objects.filter(user_id=user_id).order_by("create_date")
        ret = []
        for notice in notices:
            ret.append({
                "content": notice.content,
                "create_date": notice.create_date
            })
        return Response({"reason": "查询成功", "data": ret}, status=200)


class GetNowAnn(APIView):
    def get(self, request):
        anns = Ann.objects.filter().order_by("create_date")
        ret = []
        for ann in anns:
            ret.append({
                "content": ann.content,
                "create_date": ann.create_date
            })
        return Response({"reason": "查询成功", "data": ret}, status=200)