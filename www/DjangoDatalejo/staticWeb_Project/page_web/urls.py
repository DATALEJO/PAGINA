from rest_framework import routers
from .viewsets import ListaNavbarViewSet
from . import views
from django.urls import path, include

router = routers.SimpleRouter()
router.register('page', ListaNavbarViewSet)
#urlpatterns = router.urls
urlpatterns=[
    #router.urls,
    path('api/v1.0/', include(router.urls)),
    path('Contacto/',views.send_email),
    path('',views.index,name='index'),
    #path('contacto',views.index,name='index'),
]