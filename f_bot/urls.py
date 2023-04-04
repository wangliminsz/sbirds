"""f_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

#------------------------------------------

from django.views.static import serve
from f_bot.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL
from f_bot.settings import STATIC_ROOT

# from django.conf import settings
# from django.conf.urls.static import static


#------------------------------------------

print(MEDIA_ROOT)
print(MEDIA_URL)
print(STATIC_ROOT)
print(STATIC_URL)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('fbot_app.urls')),
]

# if settings.DEBUG:
# if True:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
if True:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # print(settings.STATIC_URL)
     
