from django.contrib import admin
from django.urls import path
from core.views import main, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('about/', AboutView.as_view()),
]
