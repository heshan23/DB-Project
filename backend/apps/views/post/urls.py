from django.urls import path

from apps.views.post.Comment import *
from apps.views.post.Post import *

urlpatterns = [
    # 获取帖子信息
    path('NewPost/', NewPost.as_view()),
    path('QueryUserPost/', QueryUserPost.as_view()),
    path('QueryAllPost/', QueryAllPost.as_view()),
    path('PostGet<int:post_id>/', PostGet.as_view()),
    path('ModifyPost<int:post_id>/', ModifyPost.as_view()),
    # 评论
    path('NewComment/', NewComment.as_view()),
]
