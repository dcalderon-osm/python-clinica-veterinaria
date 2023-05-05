# python-clinica-veterinaria

Se desea desarrollar un programa para gestionar una clínica veterinaria. El programa debe permitir registrar pacientes, crear historias clínicas, realizar consultas y operaciones, y generar informes. 

1) Crea una clase llamada Paciente que tenga los siguientes atributos: 

nombre (string): el nombre del paciente. 

especie (string): la especie del paciente (por ejemplo, "perro" o "gato"). 

raza (string): la raza del paciente. 

edad (int): la edad del paciente en años. 

peso (float): el peso del paciente en kilogramos. 

La clase Paciente debe tener un método llamado info_paciente que imprima en la consola los atributos del paciente. 

2) Crea una clase llamada HistoriaClinica que tenga los siguientes atributos: 

paciente (objeto Paciente): el paciente asociado a la historia clínica.

fecha (string): la fecha en que se crea la historia clínica. 

diagnostico (string): el diagnóstico del paciente. 

tratamiento (string): el tratamiento del paciente. 

La clase HistoriaClinica debe tener un método llamado info_historia que imprima en la consola los atributos de la historia clínica. 

3) Crea una clase llamada Consulta que tenga los siguientes atributos: 

paciente (objeto Paciente): el paciente asociado a la consulta. 

fecha (string): la fecha en que se realiza la consulta. 

motivo (string): el motivo de la consulta. 

diagnostico (string): el diagnóstico de la consulta. 
La clase Consulta debe tener un método llamado info_consulta que imprima en la consola los atributos de la consulta. 

4) Crea una clase llamada Operacion que tenga los siguientes atributos: 

paciente (objeto Paciente): el paciente asociado a la operación. 

fecha (string): la fecha en que se realiza la operación. 

tipo (string): el tipo de operación. 

diagnostico (string): el diagnóstico de la operación. 

La clase Operacion debe tener un método llamado info_operacion que imprima en la consola los atributos de la operación. 

5) Crea una clase llamada ClinicaVeterinaria que tenga los siguientes atributos: 

pacientes (lista de objetos Paciente): una lista de los pacientes de la clínica. 

historias (lista de objetos HistoriaClinica): una lista de las historias clínicas de los pacientes. 

consultas (lista de objetos Consulta): una lista de las consultas realizadas. 

operaciones (lista de objetos Operacion): una lista de las operaciones realizadas. 

La clase ClinicaVeterinaria debe tener los siguientes métodos:

registrar_paciente(paciente): este método debe recibir un objeto Paciente como parámetro y añadirlo a la lista de pacientes de la clínica. 

crear_historia(paciente, fecha, diagnostico, tratamiento): este método debe recibir un objeto Paciente, una fecha, un diagnóstico y un tratamiento como parámetros, y crear una nueva historia clínica para el paciente.

realizar_consulta(paciente, fecha, motivo, diagnostico): este método debe recibir un objeto Paciente, una fecha, un motivo y un diagnóstico como parámetros, y crear una nueva consulta para el paciente. 

realizar_operacion(paciente, fecha, tipo, diagnostico): este método debe recibir un objeto Paciente, una fecha, un tipo de operación y un diagnóstico como parámetros, y crear una nueva operación para el paciente. 
generar_informe_paciente(paciente): este método debe recibir un objeto Paciente como parámetro e imprimir en la consola todas las historias clínicas, consultas y operaciones asociadas al paciente. 

generar_informe_clinica(): este método debe imprimir en la consola un informe general de la clínica, mostrando los pacientes registrados y las historias clínicas, consultas y operaciones realizadas. 

6) Crea un programa que permita al usuario interactuar con la clínica veterinaria. El programa debe mostrar un menú con las siguientes opciones: 

Registrar un paciente. 

Crear una historia clínica. 

Realizar una consulta. 

Realizar una operación. 

Generar informe de un paciente. 

Generar informe general de la clínica. 

Salir del programa. 

Cuando el usuario selecciona una opción, el programa debe pedir los datos necesarios y llamar al método correspondiente de la clase ClinicaVeterinaria. El programa debe mostrar un mensaje de confirmación después de cada operación realizada.
