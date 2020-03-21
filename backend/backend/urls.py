from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('vocab.urls')),    #vocab
    path('accounts/', include('django.contrib.auth.urls')),         #login
    path('', include('accounts.urls')),                             #register
    path('', include('authapi.urls'))                               #login from different source
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
