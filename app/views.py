from django.shortcuts import render

# Create your views here.
def usdfilter(request):
    d={'data':'Hai HoW aRe yOu'}
    return render(request,'usdfilter.html',d)