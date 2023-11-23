from django.http import JsonResponse, HttpResponse


class FirstMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response  # stands for either view or next middleware

    def __call__(self, request):  # used for getting response
        print('FirstMiddleware before')
        # return HttpResponse('ok')  # terminates execution process
        response = self._get_response(request)
        print('FirstMiddleware after')
        return response  # response sends either to the next middleware or to client

    def process_exception(self, request, exception):
        print(f'Exception occured => {exception}')
        return HttpResponse('Exception!')


class SecondMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response  # stands for either view or next middleware

    def __call__(self, request):  # used for getting response
        print('SecondMiddleware before')
        response = self._get_response(request)
        print('SecondMiddleware after')
        return response  # response sends either to the next middleware or to client
