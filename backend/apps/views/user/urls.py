from django.urls import path

from apps.views.user.Account import *
from apps.views.user.Collection import *
from apps.views.user.Images import *
from apps.views.user.Like import *

urlpatterns = [
    # 用户账号
    path('SignUp/', UserSignUp.as_view()),
    path('SignIn/', UserSignIn.as_view()),
    path('EditProfile/', EditProfile.as_view()),
    path('YourAccountMessage/', YourAccountMessage.as_view()),
    # 用户点赞帖子
    path('Like/', Like.as_view()),
    path('UnLike/', UnLike.as_view()),
    path('hasLiked/', hasLike.as_view()),
    path('hasLikedComment/', hasLikeComment.as_view()),
    # 用户收藏
    path('Collection/', DOCollection.as_view()),
    path('UnCollection/', UnCollection.as_view()),
    # 上传图片
    path('UploadImage/', UploadImage.as_view()),
    path('GetImageUrl/', GetImageUrl.as_view()),
    path('UploadAvator/', UploadAvator.as_view()),
    # 管理员功能
    path('RemoveUser/', RemoveUser.as_view())
]
