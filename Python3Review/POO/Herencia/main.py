from Maestro import Maestro
from Administrativo import Administrativo
from Jefe import Jefe

jefe = Jefe('1231234', 'Nestor', 'Adrian', 'Lopez', 'Luque', 'En la casa de el', '123424', 'Facultad IS',
            'Maestria en BI', 'Base de datos', False, '20220101', '20250101')

print(Jefe.mro())
print(f"Datos del Jefe : {jefe}")

print(type(jefe))
# print(type(jefe) is Maestro)

print(jefe.getTipo())
print(jefe.getTipoSuper())

# administrativo = Administrativo('55555', 'Ad', 'Min', 'A', 'B', 'En la casa de el', '55555',  'Base de datos', False)
# print(administrativo.__str__(True))


administrativo = Administrativo('55555', 'Ad', 'Min', 'A', 'B', 'En la casa de el', '55555',  'Base de datos', False)
print(administrativo)