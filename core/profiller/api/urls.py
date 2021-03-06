from django.urls import path, include

from profiller.api.views import ProfilViewSet, ProfiDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kullanici-profilleri', ProfilViewSet)
router.register(r'durum', ProfiDurumViewSet, basename='durum')


#profil_list = ProfilViewSet.as_view({'get': 'list'})
#profil_detay = ProfilViewSet.as_view({'get': 'retrieve'})


urlpatterns = [

    path('', include(router.urls)),
    path('profil_foto/', ProfilFotoUpdateView.as_view(), name = 'profil-foto'),

#    path('kullanici-profilleri/', profil_list, name = 'profiller'),
#    path('kullanici-profiller/<int:pk>', profil_detay, name = 'profil-detay')
]