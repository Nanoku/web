from django.http import HttpResponse 
def test(request, *args, **kwargs, q_id = 0):
    return HttpResponse('OK')