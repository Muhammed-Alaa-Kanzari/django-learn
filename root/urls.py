from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', reviews.views.HomePage.as_view(), name='homepage')
    path('', include('reviews.urls'))

]
