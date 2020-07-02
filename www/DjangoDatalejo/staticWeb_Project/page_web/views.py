from __future__ import unicode_literals
from django.shortcuts import render
#from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view 
from page_web.forms import FormularioContacto

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())

#def mi_envio():
#    connection = mail.get_connection()
#    # Manually open the connection
#    connection.open()
#    email1 = mail.EmailMessage(
#        'Contacto Comercial',
#        'mensaje de prueba.',
#        'contactodatalejo@gmail.com',
#        ['recipient@example.com'],
#        #fail_silently=False,
#        )
#    email1.send() # Send the email

# @csrf_exempt
# @api_view(['POST'])
# #@csrf_protect
# def send_email(request):
#     #send_mail('Contacto Comercial','mensaje de prueba..','contactodatalejo@gmail.com',['contactodatalejo@gmail.com'],fail_silently=False)  
#     if request.method == 'POST':            
#         subject = request.POST.get('name', '')
#         message = request.POST.get('msg', '')
#         from_email = request.POST.get('email', '')
#         if subject and message and from_email:
#             try:
#                 send_mail(subject, message, from_email, ['contactodatalejo@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return HttpResponseRedirect('/contact/thanks/')
#         else:
#             # In reality we'd use a form class
#             # to get proper validation errors.
#             return HttpResponse('Make sure all fields are entered and valid.')
#     else:
#         return HttpResponse('Post method required.')
#@ensure_csrf_cookie()

@csrf_exempt
#@api_view(['POST'])
#@csrf_protect
def send_email(request):
    if request.method=="POST":
        infopost=request.POST
        #miForm=FormularioContacto({'name':request.POST.name,'email':request.POST.email,'msg':request.POST.msg})
        #print(aCookie)
        print(infopost)
        miForm=FormularioContacto(request.POST)
        if  miForm.is_valid():
            infoForm = miForm.cleaned_data()
            print(infoForm)
            send_mail('ContactoCliente '+infoForm['name'],infoForm['msg'],infoForm.get('email',''),
            [contactodatalejo@gmail.com],)
            #return render(request,"gracias.html")
            return HttpResponse('Gracias, te contactaremos lo antes posible.')
        else:
            miForm=FormularioContacto()
            return HttpResponse('Por favor revise que la información  ingresada sea valida')
        #return render(request,"formularioContacto.html",{"form":miForm})
        return HttpResponse('Datos No validos.')
    else:
        return HttpResponse('Formulario no cargado, por favor retroceda y envíe el un correo a contactodatalejo@gmail.com.')

        


