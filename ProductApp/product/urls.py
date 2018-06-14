from django.conf.urls import url
from . import views


urlpatterns = [    
    url(r'^get-product-records/$', views.get_product_records, name="product_record"),
    url(r'^update-product-quantity/$', views.update_product_quantity, name="product_quantity"),
    url(r'^place-orders/$', views.place_order, name="all_place_order"),
    url(r'^get-place-orders/$', views.get_place_order, name='place_order'),
    url(r'^search-product/$', views.get_search_product, name='search_product')
]