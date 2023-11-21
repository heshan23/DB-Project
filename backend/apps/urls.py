from django.urls import path, include

urlpatterns = [
    path('User/', include('apps.views.user.urls')),
    path('Post/', include('apps.views.post.urls'))
]
