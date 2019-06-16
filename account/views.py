from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    try:
        user_id = request.session['user_id']
    except:
        return HttpResponseRedirect('sign-up')



def sign_up(request):
    return render(request, 'account/sign-up.html')
