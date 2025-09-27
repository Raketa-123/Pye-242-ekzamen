from django.contrib import admin
from django.urls import path, include
from users.views import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", UserRegisterView.as_view()),
    path('', include('news.urls')),
]