from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.customers import Customer
from ..serializers.customers import CustomerSerializer
from django.core.paginator import Paginator
from ..utils import execution_time_logger
import copy

class CustomerCreateView(APIView):
    """
    API view for creating a new Customer object.

    This view handles the creation of a customer record associated with the authenticated user.
    It validates the input data against the `CustomerSerializer`, saves the record if valid, 
    and returns the created customer's data.

    Attributes:
        permission_classes (list): List of permissions required to access this view.
            This view requires the user to be authenticated.

    Methods:
        post(request, version):
            Creates a new customer record using the data provided in the request.
            Adds the authenticated user's ID to the data before validation and saving.
            Returns a 201 CREATED response with the customer data if successful, 
            or a 400 BAD REQUEST response with error details if validation fails.
    
    Args:
        request (Request): The HTTP request object containing customer data.
        version (str): API version passed in the URL.
    
    Returns:
        Response: JSON response with the newly created customer data or validation errors.
    """
    permission_classes = [IsAuthenticated]

    @execution_time_logger
    def post(self, request, version):
        request_data = copy.deepcopy(request.data)
        request_data['user'] = request.user.pk
        serializer = CustomerSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerListView(APIView):
    """
    API view for retrieving a paginated list of Customer objects for the authenticated user.

    This view fetches customer records associated with the authenticated user and returns 
    them in a paginated format. Each page contains a limited number of records as defined 
    by the `Paginator`. The page number is determined from the query parameter 'page'.

    Attributes:
        permission_classes (list): List of permissions required to access this view.
            This view requires the user to be authenticated.

    Methods:
        get(request, version):
            Retrieves a paginated list of customers for the authenticated user.
            Returns a JSON response containing customer data and the total count of customers.
    
    Args:
        request (Request): The HTTP request object, including optional 'page' query parameter.
        version (str): API version passed in the URL.
    
    Returns:
        Response: JSON response with paginated customer data and total customer count.
    """
    permission_classes = [IsAuthenticated]

    @execution_time_logger
    def get(self, request, version):
        customers = Customer.objects.filter(user=request.user)
        paginator = Paginator(customers, 5)
        page_number = request.query_params.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = CustomerSerializer(page_obj, many=True)
        return Response({"data": serializer.data, "total_customer": customers.count()})
