from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Welcome!"
    if request.user.is_authenticated():
        title = "My Title %s"%(request.user)

    context = {
        "template_title": title,
        #"abc": 123,
    }
    return render(request, "home.html", context)

