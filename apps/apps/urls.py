from django.urls import include, path
from django.contrib import admin

import theme.views

urlpatterns = [
    path('', theme.views.home),
    path('orders/', include('orders.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
