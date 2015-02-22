import json

from django.http import Http404
from django.shortcuts import redirect

from api.models import Contact

def submit_handler(request):
    if request.method != 'POST':
        return JsonResponse({})

    try:
        json_dict = json.dumps(request.POST)
        contact = Contact(info=json_dict)
        contact.save()
    except:
        raise Http404('Sorry we cannot get your response. ')

    return redirect('/contact/')
