$('#register-form').on('submit', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/1/register/',
        data: JSON.stringify({
            username: $('#username').val(),
            email: $('#email').val(),
            password: $('#password').val()
        }),
        contentType: "application/json",
        success: function(response) {
            console.log(response);
            alert('Registration successful');
            window.location.href = '/login';
        },
        error: function(xhr) {
            alert(xhr.responseJSON.detail || "Registration failed");
        }
    });
});