from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.generic import TemplateView

from movie_database.views import MainPage, LogoutView, LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^login2/', LoginView.as_view(), name='login-standard'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^$', MainPage.as_view(), name='main-page')
]