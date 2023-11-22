from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class DOCollection(APIView):
    def post(self, request):
        try:
            user_id = str(request.data["user_id"])
            post_id = str(request.data["post_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,post_id"},
                            status=422)
        try:
            user = User.objects.get(
                id=user_id
            )
            post = Post.objects.get(
                id=post_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Post.DoesNotExist:
            return Response({"reason": "错误,post_id有误"}, status=500)
        try:
            Collection.objects.create(
                user=user,
                post=post
            )
        except Exception as e:
            print(e)
            return Response({"reason": "已经收藏过了"}, status=500)
        return Response({"reason": "收藏成功"}, status=200)


class UnCollection(APIView):
    def post(self, request):
        try:
            user_id = str(request.data["user_id"])
            post_id = str(request.data["post_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,post_id"},
                            status=422)
        try:
            user = User.objects.get(
                id=user_id
            )
            post = Post.objects.get(
                id=post_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Post.DoesNotExist:
            return Response({"reason": "错误,post_id有误"}, status=500)
        try:
            Collection.objects.get(
                user=user,
                post=post
            ).delete()
        except Exception as e:
            print(e)
            return Response({"reason": "当前未收藏该帖子，无法撤销"}, status=500)
        return Response({"reason": "取消收藏"}, status=200)
