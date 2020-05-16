from django.http import HttpResponse
import datetime
from django.template import Template, Context

def salud(request):
    doc_externo=open("C:/Users/Usuario/Desktop/proyectobueno/inte/inte/templates/index.html")

    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def step1(request):
    doc2_externo=open("C:/Users/Usuario/Desktop/proyectobueno/inte/inte/templates/cap1.html")

    plt2 = Template(doc2_externo.read())
    doc2_externo.close()
    ctx2 = Context()
    documento2=plt2.render(ctx2)
    return HttpResponse(documento2)
def step2(request):
    doc3_externo=open("C:/Users/Usuario/Desktop/proyectobueno/inte/inte/templates/cap2.html")

    plt3 = Template(doc3_externo.read())
    doc3_externo.close()
    ctx3 = Context()
    documento3=plt3.render(ctx3)
    return HttpResponse(documento3)

def step3(request):
    doc4_externo=open("C:/Users/Usuario/Desktop/proyectobueno/inte/inte/templates/cap3.html")

    plt4 = Template(doc4_externo.read())
    doc4_externo.close()
    ctx4 = Context()
    documento4=plt4.render(ctx4)
    return HttpResponse(documento4)

def step4(request):
    doc5_externo=open("C:/Users/Usuario/Desktop/proyectobueno/inte/inte/templates/cap4.html")

    plt5 = Template(doc5_externo.read())
    doc5_externo.close()
    ctx5 = Context()
    documento5=plt5.render(ctx5)
    return HttpResponse(documento5)
