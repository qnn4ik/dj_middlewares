from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import transaction

from .models import *


def home(request):
    # 1/0
    return JsonResponse({'success': True})
