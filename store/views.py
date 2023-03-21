from django.shortcuts import render,HttpResponse


# Create your views here.
# def index(request):
#     # return HttpResponse("this is homepage")
#     contex = {'variable':"this is furniture store"}
#     return render(request,'item.html',contex)

def home(request):
    return render(request,'home.html')
def sofa(request):
    return render(request,'sofa.html')
def bed(request):
    return render(request,'bed.html')
def dinning(request):
    return render(request,'dinning.html')
def tables(request):
    return render(request,'tables.html')
def chairs(request):
    return render(request,'chairs.html')
def shelves(request):
    return render(request,'shelves.html')
def lamps(request):
    return render(request,'lamps.html')

