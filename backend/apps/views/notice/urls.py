from django.urls import path

from apps.views.notice.Ann import *

urlpatterns = [
    # 获取帖子信息
    path('AddAnn/', AddAnn.as_view()),
    path('GetNowNotice/', GetNowNotice.as_view()),
    path('GetNowAnn/', GetNowAnn.as_view()),
    path('ReadNotice/', ReadNotice.as_view())
]
