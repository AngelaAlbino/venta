from django.db import models
from django import forms
import datetime
CIUDADES=(
	("Sel", "--Seleccione"),
	("potosi", "POTOSI"),
	("oruro", "ORURO"),
	("lapaz", "LA PAZ"),
	("cocha", "COCHABAMBA"),
	("santacruz", "SANTA CRUZ"),
)


HORAS=(
	('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'),
	('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'),
	('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'),
	('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'),
	('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'),
	('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'),
	('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'),
	('18:30', '18:30'), ('19:00', '19:00'), ('20:30', '20:30'),
	('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'),
	('22:30', '22:30'), ('23:00', '23:00'), ('23:30', '23:30'),
	('24:00', '24:00'), 
	)

CARRILES=(
	("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),
	)

class Rutas(models.Model):
	origen=models.CharField(max_length=20, verbose_name="Origen", choices=CIUDADES)
	destino=models.CharField(max_length=20, verbose_name="Destino", choices=CIUDADES)
	distancia=models.IntegerField()
	duracion=models.CharField(max_length=50)
	cama=models.DecimalField(max_digits=10,decimal_places=2)
	semicama=models.DecimalField(max_digits=10,decimal_places=2)
	normal=models.DecimalField(max_digits=10,decimal_places=2)
	def __unicode__(self):
		return self.origen+" - "+self.destino



class Bus(models.Model):
	numero_de_placa=models.CharField(max_length=10, verbose_name="Numero_de_placa")
	nombre=models.CharField(max_length=20, null=True, verbose_name="Nombre")
	marca=models.CharField(max_length=20, null=True,verbose_name="Marca")
	tipo=models.CharField(max_length=30, verbose_name="Tipo")
	asi_izq_ven=models.IntegerField()
	asi_izq_pas=models.IntegerField()
	asi_der_ven=models.IntegerField()
	asi_der_pas=models.IntegerField()
	#fecha_registro=models.DateField(null=True)
	fecha_registro=models.DateField(auto_now=True)
	#hora_salida=models.TimeField()
	#-------------------Relacion de llaves con Rutas------------------------
	#id_ruta=models.ForeignKey(Rutas)
	#-----------------------------------------------------------------------
	def __unicode__(self):
		return self.numero_de_placa+" - "+self.marca+" - "+self.tipo

class Salidas(models.Model):
    hora=models.TimeField()
    carril=models.IntegerField()
    id_ruta=models.ForeignKey(Rutas)
    id_bus=models.ForeignKey(Bus)
    '''def __unicode__(self):
    	return''' 

'''class Salidas(models.Model):
    hora=models.TimeField()
    carril=models.IntegerField()
    id_ruta=models.ForeignKey(Rutas)
    id_bus=models.ForeignKey(Bus)'''


class Cliente(models.Model):
	nit_cliente=models.CharField(max_length=20,verbose_name="nit_ci")
	nombre_cliente=models.CharField(max_length=50, verbose_name="nombre_cliente")
	direccion=models.CharField(max_length=50,null=True)
	telefono=models.CharField(max_length=10,null=True)
	email=models.EmailField(max_length=100)
	ciudad=models.CharField(max_length='30', choices=CIUDADES)

class Usuarios(models.Model):
	nombre=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=100)
	ci=models.CharField(max_length=10)
	#rol=models.CharField (max_length=100)
	fecha_nacimiento=models.DateField()
	direccion=models.CharField(max_length=50)
	telefono=models.CharField(max_length=10)
	email=models.EmailField(max_length=100)
	nickname=models.CharField (max_length='100', verbose_name="Nickname")
	password= models.CharField (max_length='100', verbose_name="Password")
		

class Venta(models.Model):
	fecha_registro=models.DateField()
	cantida=models.CharField(max_length=10, verbose_name="Cantidad")
	costo_total=models.CharField(max_length=25, verbose_name="Costo_total")
	estado=models.CharField(max_length=10, verbose_name="Estado")
	#-------------------Relacion de llaves con BUS-------------------------
	#id_bus=models.ForeignKey(Bus)
	id_salida=models.ForeignKey(Salidas)
	#-----------------------------------------------------------------------
	id_cliente=models.ForeignKey(Cliente)
	#-----------------------------------------------------------------------
	id_usuario=models.ForeignKey(Usuarios)
	def __unicode__(self):
		return self.id_bus



class Factura(models.Model):
	N_autorizacion=models.CharField(max_length=20, verbose_name="N_autorizacion")
	nit_empresa=models.CharField(max_length=20, verbose_name="nit")
	codi_control=models.CharField(max_length=40,verbose_name="codi_control")
	fecha_emision=models.DateTimeField()
	nit_cliente=models.CharField(max_length=20, verbose_name="nit_cliente")
	nombre_cliente=models.CharField(max_length=50, verbose_name="nombre_cliente")
	origen=models.CharField(max_length=20, verbose_name="doci_ini")
	destino=models.CharField(max_length=20, verbose_name="doci_final")
	Nun_asiento=models.IntegerField()
	costo_total=models.CharField(max_length=20, verbose_name="total") 
	fecha_salida=models.DateField()
	hora_salida=models.DateField()
	codi_control=models.CharField(max_length="40",verbose_name="codi_control")


class Usuario(models.Model):
	nombre= models.CharField (max_length='50', verbose_name="Nombre")
	email= models.EmailField (verbose_name="Email")
	rol=models.CharField (max_length='100')
	nickname=models.CharField (max_length='100', verbose_name="Nickname")
	password= models.CharField (max_length='100', verbose_name="Password")
	def __unicode__(self):
		return self.nickname

class cliente(models.Model):
	nombre=models.CharField(max_length='200')
	apellidos=models.CharField(max_length='200')
	Ci=models.CharField(max_length='200')
	telefono=models.CharField(max_length='20')
	email=models.EmailField()
	direccion=models.CharField(max_length='50')
	ciudad=models.CharField(max_length='30', choices=CIUDADES,)
	def __unicode__(self):
		return "%s %s"%(self.nombre,self.Ci)
