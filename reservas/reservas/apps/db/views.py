from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from reservas.settings import RUTA_PROYECTO
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, authenticate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from models import Usuario, Rutas, Bus, Usuarios, Salidas, Venta
from forms import UsuarioForm,NuevoUsuarioForm,CambioForm
import os
import datetime
from forms import RutaForm, RutaForm2, BusForm, UsuariosForm, SalidasForm, VentaForm
import pdb

def salidasView(request):
    if request.method == "POST":
        formularioSalidas=SalidasForm(request.POST)
        #pdb.set_trace()
        if  formularioSalidas.is_valid():
            formularioSalidas.save()
            return redirect("/db/menu/")
    else:
        formularioSalidas=SalidasForm()
    return render_to_response("salidas.html", {"formularioSalidas": formularioSalidas}, context_instance=RequestContext(request))
    pass

def ventasView(request):
    formularioVenta=VentaForm()
    return render_to_response("ventas.html", {"formularioVenta": formularioVenta}, context_instance=RequestContext(request))
    #return render_to_response("ventas.html", {"formularioVenta": formularioVenta, "lista": lista}, context_instance=RequestContext(request))


'''def salidasView(request):
    formularioSalidas=SalidasForm()
    datos=Rutas.objects.all()
    return render_to_response("salidas.html", {"formularioSalidas": formularioSalidas, "datos": datos}, context_instance=RequestContext(request))
    pass'''

def usuariosView(request):
    if request.method == "POST":
        formularioUsuarios = UsuariosForm(request.POST)
        if formularioUsuarios.is_valid():
            #if formularioUsuarios.cleaned_data['password']=formularioUsuarios.cleaned_data['password2']:
            dia=formularioUsuarios.cleaned_data['fecha_nacimiento_dia']
            mes=formularioUsuarios.cleaned_data['mes']
            ano=formularioUsuarios.cleaned_data['ano']
            fecha=ano+"-"+mes+"-"+dia
            usuarios= Usuarios(
                nombre=formularioUsuarios.cleaned_data['nombre'],
                apellidos=formularioUsuarios.cleaned_data['apellidos'],
                ci=formularioUsuarios.cleaned_data['ci'],
                fecha_nacimiento=fecha,
                direccion=formularioUsuarios.cleaned_data['direccion'],
                telefono=formularioUsuarios.cleaned_data['telefono'],
                email=formularioUsuarios.cleaned_data['email'],
                nickname=formularioUsuarios.cleaned_data['nickname'],
                password=formularioUsuarios.cleaned_data['password']    
            )
            usuarios.save()
            return redirect('/db/menu/')
            #else:
    else:
        formularioUsuarios= UsuariosForm()
    return render_to_response("usuarios.html",{"formularioUsuarios": formularioUsuarios}, context_instance=RequestContext(request))


def busView(request):
    if request.method=="POST":
        formularioBus= BusForm(request.POST)
        if formularioBus.is_valid():
            bus= Bus(
                numero_de_placa=formularioBus.cleaned_data['numero_de_placa'],
                nombre=formularioBus.cleaned_data['nombre'],
                marca=formularioBus.cleaned_data['marca'],
                tipo=formularioBus.cleaned_data['tipo'],
                asi_izq_ven=formularioBus.cleaned_data['asiento_ventanilla_izquierda'],
                asi_izq_pas=formularioBus.cleaned_data['asiento_pasillo_izquierda'],
                asi_der_ven=formularioBus.cleaned_data['asiento_ventanilla_derecha'],
                asi_der_pas=formularioBus.cleaned_data['asiento_pasillo_derecha'],
                #fecha_registro=Date.now()
                #hora_salida=formularioBus.cleaned_data['hora_salida'],
                )
            bus.save()
            return redirect("/db/menu/")

            
    formularioBus=BusForm()
    return render_to_response("buses.html", {"formularioBus": formularioBus}, context_instance=RequestContext(request))

def rutasView(request):
    if request.method == "POST":
        formularioRuta = RutaForm2(request.POST)
        if formularioRuta.is_valid():
            formularioRuta.save()
            return redirect('/db/menu/turismolink/')
    else:
        formularioRuta2 = RutaForm2()
    return render_to_response("rutas.html", {"formularioRuta2": formularioRuta2}, context_instance=RequestContext(request))

'''def rutasView(request):
    if request.method == "POST":
        formularioRuta = RutaForm(request.POST)
        if formularioRuta.is_valid():
            ruta = Rutas(origen=formularioRuta.cleaned_data['origen'],
                destino=formularioRuta.cleaned_data['destino'],
                distancia=formularioRuta.cleaned_data['distancia'],
                duracion=formularioRuta.cleaned_data['duracion'],
                cama=formularioRuta.cleaned_data['cama'],
                semicama=formularioRuta.cleaned_data['semicama'],
                normal=formularioRuta.cleaned_data['normal'])
            ruta.save()
            formularioRuta.save()
            return redirect('/db/menu/turismolink/')
    else:
        formularioRuta = RutaForm()
    return render_to_response("rutas.html", {"formularioRuta": formularioRuta}, context_instance=RequestContext(request))
'''

def iniciar_sessionView(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/db/menu/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/db/menu/')
                else:
                    return HttpResponseRedirect('/db/menu/')
            else:
                return HttpResponseRedirect('/db/menu/')
    else:
        formulario = AuthenticationForm()
    return render_to_response("login.html",{'formularioangela':formulario}, context_instance=RequestContext(request))
@permission_required('auth.add_user', login_url='/db/menu/')
def nuevo_usuario(request):
	if request.method == "POST":
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/db/menu/')
	else:
		formulario = UserCreationForm()
	return render_to_response("register.html",{'formulario':formulario}, context_instance=RequestContext(request))

#@login_required(login_url='/')
def menu (request):
	return render_to_response("index.html",{},RequestContext(request))

def Login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/db/menu/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/db/menu/')
                else:
                    return HttpResponseRedirect('/db/menu/')
            else:
                return HttpResponseRedirect('/db/menu/')
    else:
        formulario = AuthenticationForm()
    return render_to_response("login.html",{'formulario':formulario}, context_instance=RequestContext(request))

#@login_required(login_url='/')
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
@permission_required('auth.add_user', login_url='/db/menu/')
def password_nuevo(request):
    if request.method == 'POST' :
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse(Login))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return  render_to_response('repassword.html', {'formulario' :formulario}, context_instance=RequestContext(request))

def sugerencia(request):
    return render_to_response("sugerencias.html",context_instance=RequestContext(request))

def reservasView(request):
    return render_to_response("reservas.html",context_instance=RequestContext(request))
    pass

def la_pazView(request):
    return render_to_response("la_paz.html",context_instance=RequestContext(request))
    pass
def oruroView(request):
    return render_to_response("oruro.html",context_instance=RequestContext(request))
    pass
def potosiView(request):
    return render_to_response("potosi.html",context_instance=RequestContext(request))
    pass
def cochabambaView(request):
    return render_to_response("cochabamba.html",context_instance=RequestContext(request))
    pass
def santa_cruzView(request):
    return render_to_response("santa_cruz.html",context_instance=RequestContext(request))
    pass