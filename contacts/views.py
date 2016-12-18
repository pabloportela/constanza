from django.http import JsonResponse
from django.http import HttpResponse
from .ContactsManager import ContactsManager
from rest_framework.renderers import JSONRenderer


def index(request):
    try:
        m = ContactsManager()
        contacts = m.get()
        return JsonResponse(contacts, safe=False)
    except:
        return HttpResponse(status=500)
