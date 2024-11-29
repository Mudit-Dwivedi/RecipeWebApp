from django.contrib import admin
from django.urls import path
from vege.views import vege
from django.conf import settings
from django.conf.urls.static import static
from vege.views import *
urlpatterns = [
    path('', vege, name="home"),        # Route for the home page
    path('recipes/', vege, name="recipes"),  # Route for the recipe submission page
    path('delete-recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),
    path('admin/', admin.site.urls),
]

# Serve media files during development
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
