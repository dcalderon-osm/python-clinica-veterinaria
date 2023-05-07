# from Paciente import Paciente as clasePaciente
from HistoriaClinica import HistoriaClinica as claseHistoria
from Consulta import Consulta as claseConsulta
from Operacion import Operacion as claseOperacion

class ClinicaVeterinaria(claseHistoria , claseConsulta , claseOperacion):
    def __init__(self):
        self.pacientes = []
        self.historias = []
        self.consultas = []
        self.operaciones = []

    @staticmethod
    def registrar_paciente(self,pacienteNuevo):
        nombre = input("Ingrese el nombre del paciente: ")
        especie = input("Ingrese la especie del paciente: ")
        raza = input("Ingrese la raza del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        peso = float(input("Ingrese el peso del paciente: "))
        pacientenuevo=pacienteNuevo(nombre,especie,raza,edad,edad,peso)
        self.pacientes.append(pacientenuevo)
        print("El paciente ha sido registrado con éxito.")

    @staticmethod
    def crear_historia(self, paciente, fecha, diagnostico, tratamiento):
        historia = (paciente, fecha, diagnostico, tratamiento)
        self.historias.append(historia)
        print("La historia clínica ha sido creada con éxito.")

    @staticmethod
    def realizar_consulta(self, paciente, fecha, motivo, diagnostico):
        consulta = (paciente, fecha, motivo, diagnostico)
        self.consultas.append(consulta)
        print("La consulta ha sido realizada con éxito.")

    @staticmethod
    def realizar_operacion(self, paciente, fecha, tipo, diagnostico):
        operacion = (paciente, fecha, tipo, diagnostico)
        self.operaciones.append(operacion)
        print("La operación ha sido realizada con éxito.")

    @staticmethod
    def generar_informe_paciente(self, paciente):
        print("Informes para el paciente", paciente.nombre)
        for historia in self.historias:
            if historia.paciente == paciente:
                historia.info_historia()
        for consulta in self.consultas:
            if consulta.paciente == paciente:
                consulta.info_consulta()
        for operacion in self.operaciones:
            if operacion.paciente == paciente:
                operacion.info_operacion()

    @staticmethod
    def generar_informe_clinica(self):
        print("Informe general de la clínica:")
        for paciente in self.pacientes:
            print(f"Paciente {paciente.nombre}:")
            for historia in paciente.historias_clinicas:
                print(historia)
            for consulta in paciente.consultas:
                print(consulta)
            for operacion in paciente.operaciones:
                print(operacion)

