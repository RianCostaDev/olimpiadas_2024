from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return render(request, "lista_medalhas/index.html", {
})

def brasil(request): 
    return render(request, "lista_medalhas/brasil.html", {
})

def estados_unidos(request): 
    return render(request, "lista_medalhas/estados_unidos.html", {
})

def uniao_sovietica(request): 
    return render(request, "lista_medalhas/uniao_sovietica.html", {
})

def japao(request): 
    return render(request, "lista_medalhas/japao.html", {
})

def china(request): 
    return render(request, "lista_medalhas/china.html", {
})

def australia(request): 
    return render(request, "lista_medalhas/australia.html", {
})

def italia(request): 
    return render(request, "lista_medalhas/italia.html", {
})

def franca(request): 
    return render(request, "lista_medalhas/franca.html", {
})

def alemanha(request): 
    return render(request, "lista_medalhas/alemanha.html", {
})

def reino_unido(request): 
    return render(request, "lista_medalhas/reino_unido.html", {
})

def coreia_do_sul(request): 
    return render(request, "lista_medalhas/coreia_do_sul.html", {
})

def canada(request): 
    return render(request, "lista_medalhas/canada.html", {
})

