from django.urls import path

from apps.views.user.Account import *

urlpatterns = [
    # 用户账号
    path('SignUp/', UserSignUp.as_view()),
    path('SignIn/', UserSignIn.as_view()),
    path('EditProfile/', EditProfile.as_view()),
    path('YourAccountMessage/', YourAccountMessage.as_view()),
    # 管理员功能

]
