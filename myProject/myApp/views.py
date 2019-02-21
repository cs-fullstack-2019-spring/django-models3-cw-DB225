from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Car

# Create your views here.
def index(request):
    return HttpResponse("Test run")

# The function that prints out all books name
def allNamesBook(request):
    allNamesBook = ""
    allBooks = Book.objects.all()

    for eachElement in allBooks:
        allNamesBook+= eachElement.name + "<br>"
    return HttpResponse(allNamesBook)

# The function that prints out all cars name
def allNamesCar(request):
    allNamesCar = ""
    allCars = Car.objects.all()

    for eachElement in allCars:
        allNamesCar+= eachElement.make + "<br>"
    return HttpResponse(allNamesCar)



# The function of the new endpoint that only prints entries with publish dates greater than or equal to 01/01/2018.
def greaterOrEqualThan01012018(request):
    objectVar = Book.objects.filter(publishedDate__gt = "2018-01-01")
    return HttpResponse(objectVar)

# The function of the model of cars greater or equal to 01/01/2010.
def greaterOrEqualThan01012010(request):
    objectVar2 = Car.objects.filter(yearAttirbutes__gt = "2010-01-01")
    return HttpResponse(objectVar2)
