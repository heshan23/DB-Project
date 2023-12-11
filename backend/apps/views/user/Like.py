from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class Like(APIView):
    def post(self, request):
        try:
            user_name = str(request.data["user_name"])
            post_id = str(request.data["post_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,post_id"},
                            status=422)
        try:
            user = User.objects.get(
                user_name=user_name
            )
            post = Post.objects.get(
                id=post_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Post.DoesNotExist:
            return Response({"reason": "错误,post_id有误"}, status=500)
        try:
            PostLike.objects.create(
                user=user,
                post=post
            )
        except Exception as e:
            print(e)
            return Response({"reason": "已经点赞过了"}, status=500)
        return Response({"reason": "点赞成功"}, status=200)


class UnLike(APIView):
    def post(self, request):
        try:
            user_name = str(request.data["user_name"])
            post_id = str(request.data["post_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,post_id"},
                            status=422)
        try:
            user = User.objects.get(
                user_name=user_name
            )
            post = Post.objects.get(
                id=post_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Post.DoesNotExist:
            return Response({"reason": "错误,post_id有误"}, status=500)
        try:
            PostLike.objects.get(
                user=user,
                post=post
            ).delete()
        except Exception as e:
            print(e)
            return Response({"reason": "当前未点赞该帖子，无法撤销"}, status=500)
        return Response({"reason": "取消点赞"}, status=200)


class LikeComment(APIView):
    def post(self, request):
        try:
            user_name = str(request.data["user_name"])
            comment_id = str(request.data["comment_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,comment_id"},
                            status=422)
        try:
            user = User.objects.get(
                user_name=user_name
            )
            comment = Comment.objects.get(
                id=comment_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Comment.DoesNotExist:
            return Response({"reason": "错误,comment_id有误"}, status=500)
        try:
            CommentLike.objects.create(
                user=user,
                comment=comment
            )
        except Exception as e:
            print(e)
            return Response({"reason": "已经点赞过了"}, status=500)
        return Response({"reason": "点赞成功"}, status=200)


class UnLikeComment(APIView):
    def post(self, request):
        try:
            user_name = str(request.data["user_name"])
            comment_id = str(request.data["comment_id"])
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id,comment_id"},
                            status=422)
        try:
            user = User.objects.get(
                user_name=user_name
            )
            comment = Comment.objects.get(
                id=comment_id
            )
        except User.DoesNotExist:
            return Response({"reason": "错误user_id有误"}, status=500)
        except Comment.DoesNotExist:
            return Response({"reason": "错误,comment_id有误"}, status=500)
        try:
            CommentLike.objects.get(
                user=user,
                comment=comment
            ).delete()
        except Exception as e:
            print(e)
            return Response({"reason": "当前未点赞该评论，无法撤销"}, status=500)
        return Response({"reason": "取消点赞"}, status=200)
