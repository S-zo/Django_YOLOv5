from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def issue(request):
    return render(request, 'issue_page.html')