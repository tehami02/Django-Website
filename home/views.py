from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context={
        "variable1":"first",
        "variable2":"second"
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def cloth(request):
    return render(request, 'cloth.html')

def void(request):
      return render(request, 'void.html')
    # return HttpResponse("this is void")

