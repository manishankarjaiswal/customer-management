if(localStorage.getItem('access_token') == null){
    window.location.href = "/login"
  }
  $('#register-form').on('submit', function(e) {
      e.preventDefault();
      $.ajax({
          type: 'POST',
          url: '/api/1/customer/create/',
          data: JSON.stringify({
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            date_of_birth: $('#date_of_birth').val(),
            phone_number: $('#phone_number').val(),
            address: $('#address').val()
          }),
          contentType: "application/json",
          headers: { 'Authorization': 'Bearer ' + localStorage.getItem('access_token') },
          success: function(response) {
              console.log(response);
              alert('Customer Added successful');
              window.location.reload();
          },
          error: function(xhr, status, error) {
            console.log(xhr, status, error)
            if(xhr.status==401){
              alert("Session Expire ! Please login again");
              window.location.href = "/login" 
            }else if(xhr.status==400){
                if("phone_number" in xhr.responseJSON){
                    alert(xhr.responseJSON["phone_number"])
                }else if("non_field_errors" in xhr.responseJSON){
                    alert("Customer with same number is not allowed.")
                }
                $("#phone_number").css("border-color", "red");
            }else{
              alert(xhr.responseJSON.detail || "Registration failed");
            }
            
          }
      });
  });