from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .router import router
from core.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/', include(router.urls))


]

urlpatterns += [
    url(r'', include(router.urls)),
    url(r'import/', HomeView.as_view()),
]
