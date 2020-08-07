from . import views
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns= [

    path('', views.store, name= 'store' ),
    path('cart/', views.cart, name= 'cart' ),
    path('checkout/', views.checkout, name= 'checkout' ),

    path('add/product/', views.addProducts, name = 'add_product'),
    path('product/<int:pk>', views.viewProduct, name = 'view_product'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)