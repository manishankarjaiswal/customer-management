from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class LoginView(APIView):
    """
    View to render the login page.

    This view handles GET requests to display the login page (`login.html`) 
    for user authentication.

    Methods:
        get(request):
            Renders the `login.html` template for user login.

    Args:
        request (Request): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered login page.
    """
    def get(self, request):
        return render(request, 'login.html')
    

class RegisterView(APIView):
    """
    View to render the registration page.

    This view handles GET requests to display the registration page (`register.html`) 
    for new users to create an account.

    Methods:
        get(request):
            Renders the `register.html` template for user registration.

    Args:
        request (Request): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered registration page.
    """
    def get(self, request):
        return render(request, 'register.html')
    

class DashboardView(APIView):
    """
    View to render the dashboard page.

    This view handles GET requests to display the user dashboard (`dashboard.html`) 
    after successful login.

    Methods:
        get(request):
            Renders the `dashboard.html` template for the user dashboard.

    Args:
        request (Request): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered dashboard page.
    """
    def get(self, request):
        return render(request, 'dashboard.html')
    

class AddCusView(APIView):
    """
    View to render the add customer page.

    This view handles GET requests to display the add customer form (`add_cus.html`) 
    where logged-in users can add new customer details.

    Methods:
        get(request):
            Renders the `add_cus.html` template for adding customer information.

    Args:
        request (Request): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered add customer page.
    """
    def get(self, request):
        return render(request, 'add_cus.html')
