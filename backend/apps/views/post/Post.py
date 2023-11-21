from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *


class NewPost(APIView):
    def post(self, request):
        try:
            username = request.data['user_name']
            title = request.data['title']
            content = request.data['content']
        except KeyError:
            return Response(
                {"reason": "keyError,请检查发送的信息是否有user_name,title,content"},
                status=422)
        try:
            user = User.objects.get(user_name=username)
            post = Post.objects.create(
                user=user,
                title=title,
                content=content,
                create_date=timezone.now()
            )
            post.save()
        except User.DoesNotExist:
            return Response(
                {"reason": "错误，用户名无效!!!"},
                status=500
            )
        return Response({
            "reason": "创建帖子成功"
        }, status=200)


# 这种查询应该是获取的简要信息，比如点赞数，评论数，然后前端选择性展示文章内容
# 而不必要全把评论展示出来
class QueryAllPost(APIView):
    def get(self, request):
        ret = []
        posts = Post.objects.filter()
        for post in posts:
            like_count = PostLike.objects.filter(post_id=post.id).count()
            comment_count = Comment.objects.filter(post_id=post.id).count()
            ret.append({
                "user_name": post.user.user_name,
                "title": post.title,
                "content": post.content,
                "create_date": post.create_date.strftime("%Y-%m-%d %H:%I:%S"),
                "like_count": like_count,
                "comment_count": comment_count
            })
        return Response({
            "reason": "查询成功",
            "data": ret,
        }, status=200)


class QueryUserPost(APIView):
    def get(self, request):
        try:
            username = request.GET['user_name']
        except KeyError:
            return Response(
                {"reason": "keyError,请检查发送的信息是否有user_name"},
                status=422)
        try:
            user = User.objects.get(user_name=username)
        except User.DoesNotExist:
            return Response({"reason": "查询用户不存在"}, status=404)
        posts = Post.objects.filter(user_id=user.id)
        ret = []
        for post in posts:
            like_count = PostLike.objects.filter(post_id=post.id).count()
            comment_count = Comment.objects.filter(post_id=post.id).count()
            ret.append({
                "post_id": post.id,
                "user_name": username,
                "title": post.title,
                "content": post.content,
                "create_date": post.create_date.strftime("%Y-%m-%d %H:%I:%S"),
                "like_count": like_count,
                "comment_count": comment_count
            })
        return Response({
            "reason": "查询成功",
            "data": ret,
        }, status=200)


class PostGet(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"reason": "无效的post id"}, status=404)
        try:
            like_count = PostLike.objects.filter(post_id=post_id).count()
            comments = []
            post_comments = Comment.objects.filter(post_id=post_id)
            tags = []
            tag_post = TagPost.objects.filter(post_id=post_id)
            for tag in tag_post:
                tags.append(tag.tag.name)
            for comment in post_comments:
                append = ""
                if comment.res_comment != -1:
                    res = Comment.objects.get(id=comment.res_comment)
                    append = (append + "@" + str(res.user.user_name) + " " +
                              str(res.content[0:min(10, len(res.content))]))
                comments.append({
                    "comment_id": comment.id,
                    "user_name": comment.user.user_name,
                    "create_date": comment.create_date,
                    "content": comment.content,
                    "append": append,
                })
        except Exception as e:
            print(e)
            return Response({"reason": "服务器错误!!!"}, status=500)
        ret = [{
            "post_id": post.id,
            "user_name": post.user.user_name,
            "title": post.title,
            "content": post.content,
            "tag": tags,
            "create_date": post.create_date.strftime("%Y-%m-%d %H:%I:%S"),
            "like_count": like_count,
            "comments": comments
        }]
        return Response({
            "reason": "查询成功",
            "data": ret,
        }, status=200)


class ModifyPost(APIView):
    def post(self, request, post_id):
        try:
            new_title = request.data['title']
            new_content = request.data['content']
        except KeyError:
            return Response({"reason": "请检查输入信息格式，是否有title和content"}, status=422)
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"reason": "无效post id"}, status=404)
        post.title = new_title
        post.content = new_content
        post.create_date = timezone.now()
        post.save()
        return Response({"reason": "修改成功"}, status=200)


'''
class CollectionPost(APIView):
    def post(self,request):
        try:
            post_id =request.data["post_id"]
            user_id = request.data["user_id"]
        except KeyError:
            return Response({"reason": "请检查输入信息格式，是否有post_id和user_id"}, status=422)
 '''
