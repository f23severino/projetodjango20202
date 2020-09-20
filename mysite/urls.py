from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('forumAvisos', include('blog2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
