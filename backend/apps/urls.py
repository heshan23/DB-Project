from django.urls import path, include

urlpatterns = [
    path('User/', include('apps.views.user.urls'))
]
