from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

# Remove this when you start your proejct
from django.views import debug

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('howdy.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
