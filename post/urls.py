from django.urls import path

from . import views
"""Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""
app_name = "post"
urlpatterns = [

path('', views.post_list, name='home'),
path('<int:id>', views.post_detail, name='home')

]
