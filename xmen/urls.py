from django.contrib import admin
from django.urls import path
from hero import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>/',views.detail),
    path('delete/<int:id>',views.delete),
    path('daftarskill/createskill/',views.createskill),
    path('daftarskill/', views.daftarskill, name="daftarskill"),
    path('detailskill/<int:id>/',views.detailskill),
    path('detailskill/<int:id>/tambahhero/',views.tambahhero),
]
