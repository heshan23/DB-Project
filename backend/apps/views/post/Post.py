from operator import itemgetter

from django.utils import timezone

from apps.views.user.Account import *
from apps.views.user.Images import image_url

default_image = image_url + '/media/images/default_background1.jpg'

default_images = [image_url + '/media/images/default_background1.jpg',
                  image_url + '/media/images/default_background2.jpg',
                  image_url + '/media/images/default_background3.jpg',
                  image_url + '/media/images/default_background4.jpg']


class NewPost(APIView):
    def post(self, request):
        try:
            username = request.data['user_name']
            title = request.data['title']
            content = request.data['content']
            board_name = request.data['board']
            tags = request.data['tags']
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
        board = Board.objects.get(name=board_name)
        try:
            board_post = BoardPost.objects.create(
                post=post,
                board=board
            )
            board_post.save()
        except Exception as e:
            print(e)
            return Response({"reason": "board-未知错误，请联系管理员"}, status=500)
        try:
            for tag in tags:
                try:
                    real_tag = Tag.objects.get(name=tag)
                except Tag.DoesNotExist:
                    real_tag = Tag.objects.create(
                        name=tag
                    )
                TagPost.objects.create(
                    tag=real_tag,
                    post=post
                )
        except Exception as e:
            print(e)
            return Response({"reason": "tag-未知错误，请联系管理员"}, status=500)
        return Response({
            "reason": "创建帖子成功"
        }, status=200)


# 这种查询应该是获取的简要信息，比如点赞数，评论数，然后前端选择性展示文章内容
# 而不必要全把评论展示出来
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
            if post.image is None:
                image = default_image
            else:
                image = post.image.img.url
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
            'image': image,
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


# 根据空不空来查询
# 默认如果不筛选的话传的是空串和空列表
class QueryPost(APIView):
    def get(self, request):
        # 节约开销,首先假设这个是none
        max_return_count = 10
        final_post = None
        good_search = True
        username = request.GET['user_name']
        try:
            # 如果是空的话，那么也会有这个键的
            user = User.objects.get(user_name=username)
            final_post = set(Post.objects.filter(
                user=user
            ).values_list("id", flat=True))
        except User.DoesNotExist as e:
            print(e)
            if username != '':
                good_search = False
        board_name = request.GET['board']
        try:
            board = Board.objects.get(name=board_name)
            if final_post is None:
                final_post = set(BoardPost.objects.filter(
                    board=board
                ).values_list("post", flat=True))
            else:
                final_post = final_post & set(BoardPost.objects.filter(
                    board=board
                ).values_list("post", flat=True))
        except Board.DoesNotExist as e:
            print(e)
            if board_name != "":
                good_search = False
        tag_list = request.GET.getlist('tags[]')
        print("this is tags :" + str(tag_list))
        try:
            # 注意,
            for tag_name in tag_list:
                print(tag_name)
                tag = Tag.objects.get(name=tag_name)
                if final_post is None:
                    final_post = set(TagPost.objects.filter(
                        tag=tag
                    ).values_list("post", flat=True))
                else:
                    final_post = final_post & set(TagPost.objects.filter(
                        tag=tag
                    ).values_list("post", flat=True))
        except Tag.DoesNotExist as e:
            print(e)
            if len(tag_list) != 0:
                good_search = False
        ret = []
        if final_post is None:
            if good_search:
                final_post = set(Post.objects.filter().values_list("id", flat=True))
            else:
                final_post = []
        i = 0
        for post_id in final_post:
            like_count = PostLike.objects.filter(post_id=post_id).count()
            comment_count = Comment.objects.filter(post_id=post_id).count()
            post = Post.objects.get(id=post_id)
            if post.image is None:
                image = default_images[i % 4]
                i = i + 1
            else:
                image = post.image.img.url
            if post.user.avatar is None:
                avatar = default_avatar_url
            else:
                avatar = post.user.avatar.img.url
            ret.append({
                "post_id": post.id,
                "writer": post.user.user_name,
                "avatar": avatar,
                "picture": image,
                "title": post.title,
                "content": post.content,
                "create_date": post.create_date.strftime("%Y-%m-%d %H:%I:%S"),
                "like_count": like_count,
                "comment_count": comment_count,
                "star_count": 0,
            })
        ret.sort(key=itemgetter("like_count"))
        ret = ret[0:max_return_count]
        return Response({
            "reason": "查询成功",
            "contents": ret,
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
