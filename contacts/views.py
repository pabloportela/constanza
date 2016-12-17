from django.http import JsonResponse
from .ContactsManager import ContactsManager


def index(request):
    m = ContactsManager()
    contacts = m.get()
    return JsonResponse(contacts, safe=False)
	
