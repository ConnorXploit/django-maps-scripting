from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def sample(request):
    return render(request, "core/sample.html")