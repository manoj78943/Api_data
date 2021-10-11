from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ok,name="ok"),
    path('deaths', views.deaths,name="Deaths"),
    path('recovered', views.recovered,name="Recovered"),
    path('active', views.active,name="Active"),
    ]