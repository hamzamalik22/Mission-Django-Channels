from django.shortcuts import render


# Create your views here.
def index(request, group_name):
    context = {"group_name": group_name}
    return render(request, "channels_app/index.html", context)
