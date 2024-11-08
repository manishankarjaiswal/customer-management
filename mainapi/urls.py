from django.urls import path
from .views.users import RegisterView, LoginView, LogoutView
from .views.customers import CustomerCreateView, CustomerListView

urlpatterns = [
    path('<int:version>/register/', RegisterView.as_view(), name='register'),
    path('<int:version>/login/', LoginView.as_view(), name='login'),
    path('<int:version>/logout/', LogoutView.as_view(), name='logout'),

    path('<int:version>/customer/create/', CustomerCreateView.as_view(), name='savecustomer'),
    path('<int:version>/customer/fetch', CustomerListView.as_view(), name='getcustomer'),
]
