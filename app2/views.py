from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'app2/signup.html')