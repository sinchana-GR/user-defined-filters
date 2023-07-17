from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'hAi maNvithA goWdA'}
    return render(request,'usdf.html',d)