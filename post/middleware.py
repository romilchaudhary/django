from django.http import HttpResponseRedirect

def auth_middleware(get_response):
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.user.id)
        url = request.META['PATH_INFO']
        if request.user.id is None:
            print("middleware")
            return HttpResponseRedirect(f'/admin/login/?next={url}')
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if request.user.id:
            print("response middleware")
        return response

    return middleware