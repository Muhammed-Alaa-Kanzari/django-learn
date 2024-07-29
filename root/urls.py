from django.contrib import admin
from django.urls import path, include
from .admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    # path('', reviews.views.HomePage.as_view(), name='homepage')
    path('', include('reviews.urls'))

]
