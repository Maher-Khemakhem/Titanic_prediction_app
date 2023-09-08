from django.urls import path
from . import views
urlpatterns = [
    path('',views.predict,name='predict'),
    path('predict/',views.submit_prediction,name='submit_prediction'),
    path('results/',views.view_results,name='results'),
]