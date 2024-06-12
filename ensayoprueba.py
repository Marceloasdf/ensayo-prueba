import os
import time
import msvcrt
trabajadores=[]
def agregar_trabajador(p_nombre_apellido,p_cargo,p_sueldo_bruto,p_desc_salud,p_desc_afp,p_sueldo_liquido):
    trabajador=[]
    trabajador.append(p_nombre_apellido)
    trabajador.append(p_cargo)
    trabajador.append(p_sueldo_bruto)
    trabajador.append(p_desc_salud)
    trabajador.append(p_desc_afp)
    trabajador.append(p_sueldo_liquido)
    trabajadores.append(trabajador)


while True:
    print("""
    1) Registrar trabajador
    2) listar todos los trabajadores
    3) imprimir planilla de sueldos
    4) salir""")
    
    while True:
        opc=int(input("seleccione su opcion deseada: "))
        if opc>=1 and opc<5:
            break

    if opc==1:
            print("registrar trabajador")
            nombre_apellido=input("ingrese nombre y apellido: ")
            cargo=input("ingrese su cargo (CEO, desarrollador, analista de datos): ")
            try:
                 sueldo_bruto=int(input("ingrese su sueldo bruto:"))
            except:
                      print("No puede escribir caracteres")
            else:
                 print("solo se puede escribir numeros")
            desc_salud=sueldo_bruto*7/100
            desc_afp=sueldo_bruto*12/100
            sueldo_liquido=sueldo_bruto-desc_salud-desc_afp
            trabajador=[]
            agregar_trabajador(nombre_apellido,cargo,sueldo_bruto,desc_salud,desc_afp,sueldo_liquido)

        
    elif opc==2:
        print("listar todos los trabajadores")
        print("orden de los numeros:")
        print("Trabajador,Cargo,sueldo bruto, desc.salud, desc.afp, liquido a pagar")
        for x in trabajadores:
             print(x)
    
    elif opc==3:
        print("imprimir planilla de sueldos")
        #como se hace esta wea ayuda
        with open('planilla_sueldos.txt','w') as archivo:
            archivo.write(nombre_apellido )
            archivo.write(cargo )
            archivo.write(sueldo_bruto )
            archivo.write(desc_salud )
            archivo.write(desc_afp )
            archivo.write(sueldo_liquido )        
    else:
         print("adios!")
