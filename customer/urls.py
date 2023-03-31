from django.urls import path
from . import views
urlpatterns=[
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('project/create', views.CustomerCreateView.as_view(), name='customer_create'),
    path('task/create', views.TaskCreateView.as_view(), name='task_create'),
    path('project/edit/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('project/delete/<int:pk>', views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),

]