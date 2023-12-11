from django.urls import path

from apps.views.post.Board import *
from apps.views.post.Comment import *
from apps.views.post.Post import *

urlpatterns = [
    # 获取帖子信息
    path('NewPost/', NewPost.as_view()),
    path('PostGet/', PostGet.as_view()),
    path('ModifyPost<int:post_id>/', ModifyPost.as_view()),
    path('QueryPost/',QueryPost.as_view()),
    # 评论
    path('NewComment/', NewComment.as_view()),
    # 新建版块
    path('AddNewBoard/', AddNewBoard.as_view()),
]
