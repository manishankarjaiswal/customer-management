if(localStorage.getItem('access_token') == null){
    window.location.href = "/login"
  }

$('#add-customer').on('click', function() {
    window.location.href = "/add-customer"
});

function updateQueryParam(url) {
    // Split URL into base and query string
    let [baseUrl, queryString] = url.split('?');
  
    // Parse query string into key-value pairs
    let queryParams = new URLSearchParams(queryString);
  
    // Get the query parameter
    let value = queryParams.get("page");
    if(value == null){
        value = 0
    }

    // Update or add the query parameter
    queryParams.set("page", parseInt(value)+1);
  
    // Rebuild and return the updated URL
    return `${baseUrl}?${queryParams.toString()}`;
  }

$('#next-btn').on('click', function() {
    let url = window.location.href
    window.location.href = updateQueryParam(url);
});

$('#logout-button').on('click', function() {
    const refreshToken = localStorage.getItem('refresh_token');
    $.ajax({
        type: 'POST',
        url: '/api/1/logout/',
        data: JSON.stringify({ refresh: refreshToken }),
        contentType: "application/json",
        headers: { 'Authorization': 'Bearer ' + localStorage.getItem('access_token') },
        success: function(response) {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            alert('Logout successful');
            window.location.href = "/login"
        },
        error: function(xhr) {
            alert("Logout failed or Session Expire ! Please login again");
            window.location.href = "/login"
        }
    });
});

$(document).ready(function() {     
    // Get the URL parameter 'page' if it exists, or set default URL
    const urlParams = new URLSearchParams(window.location.search);
    const page = urlParams.get('page');
    const fetchUrl = page ? `/api/1/customer/fetch?page=${page}` : '/api/1/customer/fetch';       
    $.ajax({
        url: fetchUrl,
        type: 'GET',
        contentType: "application/json",
        headers: { 'Authorization': 'Bearer ' + localStorage.getItem('access_token') },
        success: function(response) {
            $("#cus-count").text(response.total_customer);
            response = response.data
            for(var i=0;i<response.length;i++)
            {                    
                content = "<div class='item1'><h3 class='t-op-nextlvl'>"+response[i]['first_name']+" "+response[i]['last_name']+"</h3><h3 class='t-op-nextlvl'>"+response[i]['phone_number']+"</h3><h3 class='t-op-nextlvl'>"+response[i]['date_of_birth']+"</h3><h3 class='t-op-nextlvl'>"+response[i]['address']+"</h3></div>"
                $("#customer-items").append(content);
            }
        },
        error: function(xhr, status, error) {
            window.location.href = 'login';
        }
    });
    
});