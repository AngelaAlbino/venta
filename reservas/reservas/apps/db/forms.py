
#encodign UTF-8
from django import forms
from django.forms import ModelForm
from models import *
#import timezone
ROLES=(
	('sel', '--Porfavor Seleccione--'),
	('gerente','Gerente'),
	('admin','Administrador'),
	('secre','Secretaria'),)

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

class UsuarioForm(ModelForm):
	class Meta():
		model=Usuario
		fields=["nickname", "password"]

class NuevoUsuarioForm(ModelForm):
	nombre=forms.CharField(error_messages={"required": "El campo nombre esta vacio"})
	email=forms.EmailField(error_messages={"required": "El campo email esta vacio"})
	rol=forms.CharField(widget=forms.Select(choices=ROLES),error_messages={"required":"Elija un rol por favor"})
	nickname=forms.CharField(error_messages={"required":"El campo nickname es obligatoria"})
	password=forms.CharField(widget=forms.PasswordInput)
	repita_password=forms.CharField(widget=forms.PasswordInput)
	class Meta ():
		model=Usuario

class newpass(forms.Form):
	actual_password=forms.CharField(widget=forms.PasswordInput)
		

class CambioForm(ModelForm):
	password= forms.CharField (widget=forms.PasswordInput)
	nuevo= forms.CharField (widget=forms.PasswordInput)
	renuevo=forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model=Usuario
		fields=["password"]

class RutaForm(forms.Form):
	#id_rutas= forms.CharField()
	origen=forms.CharField(widget=forms.Select(choices=CIUDADES),error_messages={"required": "Seleccione un opcion por favor"})
	destino=forms.CharField(widget=forms.Select(choices=CIUDADES),error_messages={"required": "Seleccione un opcion por favor"})
	distancia=forms.IntegerField(error_messages={"required": "Selecciones una distancia en Kilometros"})
	duracion=forms.IntegerField(error_messages={"required" :"Campo requerido"})
	cama=forms.IntegerField(error_messages={"required" :"Campo requerido"})
	semicama=forms.IntegerField(error_messages={"required" :"Campo requerido"})
	normal=forms.IntegerField(required=True)

class RutaForm2(ModelForm):
	class Meta:
		model=Rutas

TIPOS=(
	("sel", "--SELECCIONE--"),
	("CAMA", "BUS CAMA"),
	("SEMICAMA", "BUS SEMICAMA"),
	("NORMAL", "BUS NORMAL"),
	)

class BusForm(forms.Form):
	numero_de_placa=forms.CharField(error_messages={"required": "Introdusca una placa por favor"})
	nombre=forms.CharField(error_messages={"required": "Introdusca el nombre del bus"})
	marca=forms.CharField(error_messages={"required": "Introdusca la marca del bus"})
	tipo=forms.CharField(widget=forms.Select(choices=TIPOS), error_messages={"required": "Introdusca el nombre del bus"})
	asiento_ventanilla_izquierda=forms.IntegerField(error_messages={"required": "Introdusca el numero de asientos"})
	asiento_pasillo_izquierda=forms.IntegerField(error_messages={"required": "Introdusca el numero de asientos"})
	asiento_ventanilla_derecha=forms.IntegerField(error_messages={"required": "Introdusca el numero de asientos"})
	asiento_pasillo_derecha=forms.IntegerField(error_messages={"required": "Introdusca el numero de asientos"})

	#fecha_registro=forms.DateField(error_messages={"required": "Introdusca la fecha de registro"})
	#hora_salida=forms.TimeField(widget=forms.TimeInput(), error_messages={"required": "No se introdujo una hora de salida"})#Verificar si esto va aqui
	#hora_salida=forms.TimeField(widget=forms.Select(choices=HORAS), error_messages={"required": "No se introdujo una hora de salida"})#Verificar si esto va aqui

	    # TODO: Define form fields here

class VentaForm(forms.Form):
	#fecha_registro=forms.DateField(error_messages={"required": "registre por favor"})
	cantidad=forms.CharField(error_messages={"required": "Introdusca el nombre del bus"})
	costo_total=forms.CharField(error_messages={"required": "Introdusca la marca del bus"})
	asiento=forms.CharField(error_messages={"required": "registre por favor"})
	
	#precio=forms.CharField(error_messages={"required": "registre por favor"})
'''class VentaForm(forms.Form):
	class Meta():
		model=Venta'''
    # TODO: Define form fields here
    
	
class ClienteForm2(forms.Form):
	#nit_cliente=forms.DateField(error_messages={"required": "registre por favor"})
	nit_cliente=forms.CharField(error_messages={"required": "registre por favor"})
	cantidad=forms.CharField(error_messages={"required": "Introdusca el nombre del bus"})
	costo_total=forms.CharField(error_messages={"required": "Introdusca la marca del bus"})
	asiento=forms.CharField(error_messages={"required": "registre por favor"})
	nombre_cliente=forms.CharField(error_messages={"required": "Introdusca nombre y apellido Porfavor"})
	direccion=forms.CharField(error_messages={"required": "registre porfavor"})
	telefono=forms.IntegerField(error_messages={"required": "registre porfavor"})
	email=forms.EmailField(error_messages={"required": "registre porfavor"})
	ciudad=forms.CharField(error_messages={"required": "registre porfavor"})
	
class ClienteForm(forms.Form):
	nit_cliente=forms.CharField(error_messages={"required": "registre por favor"})
    
		

DIAS=(
	('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '1990'),  ('08', '08'), ('09', '09'), ('10', '10'),
	('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),
	('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'),
	('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'),
	)
MESES=(
	 ('01', 'ENERO'), ('02', 'FEBRERO'), ('03', 'MARZO'), ('04', 'ABRIL'), ('05', 'MAYO'), ('06', 'JUNIO'), ('07', 'JULIO'),
	 ('08', 'AGOSTO'), ('09', 'SEPTIEMBRE'), ('10', 'OCTUBRE'), ('11', 'NOVIEMBRE'), ('12', 'DICIEMBRE'),
	)
ANOS=(
	 ('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'),
	 ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'),
	 ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'),
	 ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'),
	 ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'),
	 ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'),
	 ('2012', '2012'), ('2013', '2013'), ('2014', '2014'),
	)

class UsuariosForm(forms.Form):
	nombre=forms.CharField(error_messages={"required": "Registre su nombre por favor"})
	apellidos=forms.CharField(error_messages={"required": "Se requiere sus apellidos"})
	ci=forms.CharField(error_messages={"required": "Se requiere su Numero de CI"})
	
	fecha_nacimiento_dia=forms.CharField(widget=forms.Select(choices=DIAS), error_messages={"required": "Se requiere su fecha de nacimiento"})
	mes=forms.CharField(widget=forms.Select(choices=MESES), error_messages={"required": "Se requiere su fecha de nacimiento"})
	ano=forms.CharField(widget=forms.Select(choices=ANOS), error_messages={"required": "Se requiere su fecha de nacimiento"})

	direccion=forms.CharField(error_messages={"required": "Se requiere su direccion"})
	telefono=forms.CharField(error_messages={"required": "Se requiere su telefono"})
	email=forms.EmailField(error_messages={"required": "Se requiere su Email"})
	nickname=forms.CharField(error_messages={"required": "Ponga un nombre de usuario"})
	password=forms.CharField(widget=forms.PasswordInput, error_messages={"required": "Coloque una contrasena"})
	password2=forms.CharField(widget=forms.PasswordInput, error_messages={"required": "Escriba nuevamente su contrasena"})
    # TODO: Define form fields here


class SalidasForm(ModelForm):
	class Meta:
		model=Salidas

class FacturaForm(ModelForm):
    class Meta:
        model = Factura
    

'''class SalidasForm(forms.Form):	
	hora_salida=forms.TimeField(widget=forms.Select(choices=HORAS), error_messages={"required": "No se introdujo una hora de salida"})'''
    # TODO: Define form fields here