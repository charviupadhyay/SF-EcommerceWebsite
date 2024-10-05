from os import path
from django import urls, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('/', views.product_form, name='product_form')
    urls(r'^$', views.HomePage.as_view(), name='home'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)