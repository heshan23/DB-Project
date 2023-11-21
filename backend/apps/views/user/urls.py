from django.urls import path

from apps.views.user.Account import *
from apps.views.user.Like import *

urlpatterns = [
    # 用户账号
    path('SignUp/', UserSignUp.as_view()),
    path('SignIn/', UserSignIn.as_view()),
    path('EditProfile/', EditProfile.as_view()),
    path('YourAccountMessage/', YourAccountMessage.as_view()),
    # 用户点赞
    path('Like/', Like.as_view()),
    path('UnLike/', UnLike.as_view()),
    path('LikeComment/', LikeComment.as_view()),
    path('UnLikeComment/', UnLikeComment.as_view())
    # 管理员功能

]
