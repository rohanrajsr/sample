from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request,'app1/about.html')    