from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context ={
        "my_text":"this is a contect text",
        "my_number":1234,
        "my_list":[123,534,5532,765,897],
        "my_html":"<h1>Hello world</h1>"
    }
    return render(request, "about.html", my_context)