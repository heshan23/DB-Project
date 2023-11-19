from django.urls import path

from happends.views.user import Account as UA

urlpatterns = [
    # 用户账号
    path('UserSignUp/', UA.UserSignUp.as_view()),
    path('UserSignIn/', UA.Login.as_view()),
    path('YourAccountMessage/', UA.YourAccountMessage.as_view()),
    path('TryNewReg/', UA.TryAutoReg.as_view())
    # 管理员功能

]
