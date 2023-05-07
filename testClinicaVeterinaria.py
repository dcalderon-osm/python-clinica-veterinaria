from ClinicaVeterinaria import ClinicaVeterinaria
opcion = None


while opcion != 7:
    try:
        print("Opciones:")
        print("1.Registrar un paciente")
        print("2.Crear una historia clinica")
        print("3.Realizar una consulta")
        print("4.Realizar una operacion")
        print("5 informe de un paciente")
        print("6 Crear un informe general de la clinica ")
        print("7.Salir del programa")
        opcion=int(input("Escribe tu opcion(1-7): "))
    except Exception as e:
       print(f"Ocurrio un error:{e}".center(100,"-"))

    try:
        if opcion < 1 :
         print("Numero no deseado".center(100,"-"))
        elif opcion > 7:
         print("Numero no deseado".center(100,"-"))
        elif opcion == 1:
         ClinicaVeterinaria.registrar_paciente()
        elif opcion ==2:
         ClinicaVeterinaria.crear_historia(input("Crear una historia nueva:"))
        elif opcion == 3:
         ClinicaVeterinaria.realizar_consulta(input("Añadir una consulta:"))
        elif opcion == 4:
         ClinicaVeterinaria.realizar_operacion(input("Añadir una operacion:"))
        elif opcion == 5:
         ClinicaVeterinaria.generar_informe_paciente(input("Añadir un informe del paciente:"))
        elif opcion == 6:
         ClinicaVeterinaria.generar_informe_clinica(input("Añadir un informe general de la clinica:"))
    finally:
        print("")
else:
     print("Programa Finalizado Hasta la proxima".center(50,"-"))
