from django.contrib import admin
from django.urls import path
from . import views  # Import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.jobportal_view, name='jobportal'),  # Job portal view
    # path('news/add-news/', views.add_news, name='add_news'),
    # path('jobportal/add-opportunity/', views.add_opportunity, name='add_opportunity')
    path('<str:opportunity_type>/<int:opportunity_id>/', views.apply_view, name='apply'),
]
