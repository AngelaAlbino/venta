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
import os
import datetime
from forms import *
import pdb

def facturarView(request):
    if request.method=='POST':
        formulario=FacturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            redirect("/db/menu/")
        else:
            return render_to_response("facturar.html", {"formulario": formulario,"algo":"No estan los datos correctos"}, context_instance=RequestContext(request))
            pass
    '''v=Venta.objects.filter(id=1)
    s=Salidas.objects.filter(id=v.id_salida)
    b=Bus.objects.filter(id=s.id_bus)
    r=Ruta.objects.filter(id=s.id_ruta)
    c=Cliente.objects.filter(id=v.id_cliente)'''
    formulario=FacturaForm()
    #,"v":v,"s":s,"b":b,"r":r,"c":c
    return render_to_response("facturar.html", {"formulario": formulario}, context_instance=RequestContext(request))
    pass

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
    algo=""
    if request.method == 'POST' :
        formulario2=newpass(request.POST)
        if formulario2.is_valid():
            contrasena=request.POST['actual_password']
            usuario=request.user
            acceso=authenticate(username=usuario,password=contrasena)
            if acceso is not None:
                formulario = AdminPasswordChangeForm(user=usuario, data=request.POST)
                if formulario.is_valid():
                    formulario.save()
                    logout(request)
                return HttpResponseRedirect("/db/menu/loginlink/")
                pass
            else:
                formulario = AdminPasswordChangeForm(user=request.user)
                formulario2 = newpass()
                algo="Las contrasena actual no es la misma"
                return render_to_response('repassword.html', {'formulario' :formulario, "formulario2": formulario2, "algo": algo}, context_instance=RequestContext(request))
            pass
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
        formulario2 = newpass()
    return  render_to_response('repassword.html', {'formulario' :formulario, "formulario2": formulario2}, context_instance=RequestContext(request))

def sugerencia(request):
    rutas=Rutas.objects.all()
    salidas=Salidas.objects.all().values('id_ruta_id').distinct()
    usuario=request.user
    return render_to_response("sugerencias.html",{"consulta": rutas, "salidas": salidas,"usuario":usuario}, context_instance=RequestContext(request))

def reservasView(request,idrutas,tipo,precio):
    if request.method=="POST":
        formu1=VentaForm(request.POST)
        formu2=ClienteForm(request.POST)
        if formu1.is_valid() and formu2.is_valid():
            #cantidad=len(Cliente.objects.filter(nit_cliente=formu2.cleaned_data['nit_cliente']))
            cantidad=len(Cliente.objects.filter(nit_cliente=request.POST['nit_cliente']))
            if cantidad==0:
                formu3=ClienteForm2()
                cuantos=formu1.cleaned_data['cantidad']
                total=formu1.cleaned_data['costo_total']
                asiento=formu1.cleaned_data['asiento']
                nit=formu2.cleaned_data['nit_cliente']
                idbus=request.POST['id_bus']
                return render_to_response("registro.html", {"formu3": formu3,"cuantos":cuantos,"total":total,"asiento":asiento,"nit":nit,"idrutas":idrutas,"idbus":idbus}, context_instance=RequestContext(request))
            else:
                dato=Cliente.objects.get(nit_cliente=formu2.cleaned_data['nit_cliente'])
                salida=Salidas.objects.get(id_bus=request.POST['id_bus'])
                #valor=dato.id
                #print valor+"<-- Esto"
                usuario=request.user
                if usuario == None:
                    stado="RESERVADO"
                else:
                    stado="VENDIDO"
                v=Venta(
                    #fecha_registro=Date.now(),
                    cantida=formu1.cleaned_data['cantidad'],
                    costo_total=formu1.cleaned_data['costo_total'],
                    estado=stado,
                    numero_de_asiento=formu1.cleaned_data['asiento'],
                    id_salida=salida,#Buscar como asignar la salida
                    id_cliente=dato,
                    #id_usuario='1',
                )
                v.save()
                return redirect('/db/menu/turismolink/')
                pass
            pass
    bus=Bus.objects.all()
    salidas=Salidas.objects.filter(id_ruta_id=idrutas)
    formulario0=VentaForm()
    formulario1=ClienteForm()
    #"AIV": AIV, "AIP": AIP, "ADV": ADV, "ADP": ADP
    return render_to_response("reservas.html", {"salidas": salidas, "bus": bus, "tipo": tipo, "precio": precio,"formulario0": formulario0, "formulario1": formulario1}, context_instance=RequestContext(request))
    pass

def guardadoView(request):
    if request.method=='POST':
        formu3=ClienteForm2(request.POST)
        if formu3.is_valid():
            dato=len(Cliente.objects.filter(nit_cliente=request.POST['nit_cliente']))
            if dato==0:
                c=Cliente(
                    nit_cliente=formu3.cleaned_data['nit_cliente'],
                    nombre_cliente=formu3.cleaned_data['nombre_cliente'],
                    direccion=formu3.cleaned_data['direccion'],
                    telefono=formu3.cleaned_data['telefono'],
                    email=formu3.cleaned_data['email'],
                    ciudad=formu3.cleaned_data['ciudad'],
                )
                c.save()
            else:
                return render_to_response("algo.html",{"v":'El usuario y la reserva ya se guardaron'},context_instance=RequestContext(request))
                pass
            dato=Cliente.objects.get(nit_cliente=formu3.cleaned_data['nit_cliente'])         
            salida=Salidas.objects.get(id_bus=request.POST['id_bus'])
            #valor=dato[0].id
            usuario=request.user
            if usuario == None:
                stado="RESERVADO"
            else:
                stado="VENDIDO"
            v=Venta(
                    #fecha_registro=Date.now(),
                    cantida=formu3.cleaned_data['cantidad'],
                    costo_total=formu3.cleaned_data['costo_total'],
                    estado=stado,
                    numero_de_asiento=formu3.cleaned_data['asiento'],
                    id_salida=salida,#Buscar como asignar la salida
                    id_cliente=c,
                    #id_usuario='1',
                )
            v.save()
            return redirect('/db/menu/turismolink/')
        else:
            return render_to_response("algo.html",{"v":"Ocurrio un error"},context_instance=RequestContext(request))
            pass
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