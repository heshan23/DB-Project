from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class NewComment(APIView):
    def post(self, request):
        res_id = None
        try:
            # username应当是发表评论的
            username = request.data['user_name']
            post_id = request.data['post_id']
            content = request.data['content']
        except KeyError:
            return Response(
                {"reason": "keyError,请检查发送的信息是否有user_name,post_id,content"},
                status=422)
        try:
            res_id = request.data['res_id']
        except KeyError as e:
            print(e)
        try:
            user = User.objects.get(user_name=username)
            post = Post.objects.get(id=post_id)
            be_call_user = post.user
            cur = ""
            if len(content) > 10:
                cur = "..."
            if res_id is not None:
                comment = Comment.objects.get(id=res_id)
                be_call_user = comment.user
            if user != be_call_user:
                notice = Notice.objects.create(
                    user=be_call_user,
                    content=str(username) + " 回复了你: " + str(content[0:min(10, len(content))]) + cur,
                    create_date=timezone.now(),
                    related_post=post
                )
                notice.save()
            if res_id is not None:
                comment = Comment.objects.create(
                    user=user,
                    post=post,
                    content=content,
                    create_date=timezone.now(),
                    res_comment=res_id
                )
                comment.save()
            else:
                comment = Comment.objects.create(
                    user=user,
                    post=post,
                    content=content,
                    create_date=timezone.now()
                )
                comment.save()
        except User.DoesNotExist:
            return Response(
                {"reason": "错误，用户名无效!!!"},
                status=500
            )
        except Post.DoesNotExist:
            return Response(
                {"reason": "错误，帖子id无效!!!"},
                status=500
            )
        return Response({
            "reason": "创建评论成功"
        }, status=200)
