from django.urls import path, include, re_path
from django.views.static import serve

import backend.settings
urlpatterns = [
    path('User/', include('apps.views.user.urls')),
    path('Post/', include('apps.views.post.urls')),
    path('Notice/', include('apps.views.notice.urls')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': backend.settings.MEDIA_ROOT}),
]
