from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm

def home(request):
    title = "Welcome!"
    #if request.user.is_authenticated():
    #    title = "My Title %s"%(request.user)

    form = SignUpForm()
    context = {
        "template_title": title,
        #"abc": 123,
        "form": form
    }
    return render(request, "home.html", context)

