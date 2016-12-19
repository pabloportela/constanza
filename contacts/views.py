from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .ContactsManager import ContactsManager
import logging

logger = logging.getLogger(__name__)

@cache_page(60 * 5)
def index(request):
    """
    Returns an http response in json format with the parsed contacts information
    from some predefined storage.
    """
    if request.method != 'GET':
        return(JsonResponse(status=501))

    try:
        m = ContactsManager()
        contacts = m.get()
        return JsonResponse(contacts, safe=False)
    except Exception as e:
        logger.error(e)
        return HttpResponse(status=500)
