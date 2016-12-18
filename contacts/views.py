from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .ContactsManager import ContactsManager


@cache_page(60 * 5)
def index(request):
    try:
        m = ContactsManager()
        contacts = m.get()
        return JsonResponse(contacts, safe=False)
    except Exception as e:
        print(e) 
        return HttpResponse(status=500)
