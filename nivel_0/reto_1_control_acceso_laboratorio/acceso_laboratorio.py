sensor = input("Hay gas en el laboratorio?: ").lower()=="si"
equipo = input("Tienes el equipo de seguridad puesto?: ").lower()=="si"
id = int(input("Digita tu id: "))

if sensor==True:
    print("Acceso denegado por seguridad")
elif (id==id_acceso)and(equipo==True):
    print("Acceso autorizado")
else:
    print("Equipo incompleto")