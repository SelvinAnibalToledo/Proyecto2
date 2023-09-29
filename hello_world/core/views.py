from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

#  AGREGAR EL PARAMETRO book_id
def book(request, book_id):
    context = books[book_id]
    return render(request, "book.html", context)

books = {
    1:{
        "titulo": "Django example",
        "autor": "Juan hola"
    },
    2:{
        "titulo": "Django example 2",
        "autor": "Juan adios"
    },
    3:{
        "titulo": "Django example 3",
        "autor": "Juan talameda"
    },
    4:{
        "titulo": "Django example 4",
        "autor": "Juan Chavez"
    },
}