from django.contrib import admin

# Register your models here.
#from someotherapp.models import someotherMedels

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    #class Meta:
    #    model = SignUp
admin.site.register(SignUp, SignUpAdmin)



