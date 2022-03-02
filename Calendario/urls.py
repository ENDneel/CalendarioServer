from django.urls import path
from . import views
from rest_framework import routers
from .views import CalendarioUpdateView, guardarEvento, CalendarioUpdateView,guardarAnuncio,AnuncioListView
from .viewsets import AnuncioViewSet,CalendarioViewSet
from django.contrib.auth.decorators import login_required

router = routers.SimpleRouter()
router.register(r'api/anuncio', AnuncioViewSet)
router.register(r'api/calendario', CalendarioViewSet)

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout', views.logout,name='logout'),
    path('',login_required(views.CalendarioListView.as_view(),login_url="/login/"),name='dashboard'),
    path('Calendario/add/',guardarEvento,name='addEvento'),
    path('<int:pk>/update',login_required(CalendarioUpdateView.as_view(),login_url="/login/"),name='update_calendar'),
    path('Anuncio/add/',guardarAnuncio,name='create_anuncio'),
    path('Anuncio/',login_required(AnuncioListView.as_view(),login_url="/login/"),name='list_anuncio'),
    path('delete/<int:pk>/', views.image_delete, name='image_delete'),
    path('register/', views.register_user, name="register"),

]
urlpatterns += router.urls