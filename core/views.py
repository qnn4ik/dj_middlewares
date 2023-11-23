from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import transaction

from .models import *


def first_insert():
    Core.objects.create()
    raise Exception("Some problem")


def second_insert():
    Core.objects.create()


def home(request):
    first_insert()
    second_insert()
    return JsonResponse({'success': True})
