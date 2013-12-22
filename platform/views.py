from django.shortcuts import render_to_response
def login(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    import pdb;pdb.set_trace()
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response(request, 'platform/login.html')
            # Redirect to a success page.
        else:
            return render_to_response(request, 'platform/login-deactivated.html')
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        return render_to_response(request, 'platform/login-invalid.html')
