# coding=utf-8

import random
from django.http import HttpResponse


def log_middleware(get_response):
    def middleware(request):
        # antes de qualquer view
        if random.randint(1, 10) == 2:
            return HttpResponse('Deu ruim')
        response = get_response(request)
        # depois de qualquer view
        return response
    return middleware
