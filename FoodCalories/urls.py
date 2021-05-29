from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from FoodLibrary import views
from FoodLibrary.views import tagged

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FoodLibrary.urls')),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('about/', views.about, name='about'),
    path('tag/<slug:slug>/', tagged, name="tagged"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
