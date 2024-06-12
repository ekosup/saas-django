from django.shortcuts import render

from visits.models import PageVisit


def homepage(request):
    PageVisit.objects.create(path=request.path)
    context = {
        "page_title": "Home Page",
        "content": "Welcome to the home page.",
        "page_visit": PageVisit.objects.filter(path=request.path).count(),
        "total_visits": PageVisit.objects.count(),
    }
    return render(request, "home.html", context)
