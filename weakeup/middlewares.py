import json
from django.http import HttpResponse

class JsonDebugToolbarMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        if response['Content-Type'] == 'application/json':
            content = json.dumps(json.loads(response.content), sort_keys=True, indent=2)
            response = HttpResponse('<body><pre>{}</pre></body>'.format(content))

        # Code to be executed for each request/response after
        # the view is called.
        return response
