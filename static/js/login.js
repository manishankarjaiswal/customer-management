$('#login-form').on('submit', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/1/login/',
        data: JSON.stringify({
            username: $('#username').val(),
            password: $('#password').val()
        }),
        contentType: "application/json",
        success: function(response) {
            localStorage.setItem('access_token', response.access);
            localStorage.setItem('refresh_token', response.refresh);
            window.location.href = '/?page=1';
        },
        error: function(xhr) {
            alert(xhr.responseJSON.detail || "Login failed");
            $("#username").css("border-color", "red");
            $("#password").css("border-color", "red");
        }
    });
});