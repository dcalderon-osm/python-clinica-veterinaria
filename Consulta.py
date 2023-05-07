from Paciente import Paciente

class Consulta(Paciente):
    def __init__(self,paciente,fecha,motivo,diagnostico):
        super().__init__(paciente.nombre,paciente.especie, paciente.raza, paciente.edad, paciente.peso)
        self._fecha = fecha
        self._motivo = motivo
        self._diagnostico = diagnostico

    def info_consulta(self):
        return f"Fecha de la consulta:[{self._fecha}],Motivo de la consulta:[{self._motivo}],Diagnostico:[{self._diagnostico}]"


    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha


    @property
    def motivo(self):
        return self._motivo
    @motivo.setter
    def motivo(self,motivo):
        self._motivo = motivo


    @property
    def diagnostico(self):
        return self._diagnostico
    @diagnostico.setter
    def diagnostico(self,diagnostico):
        self._diagnostico = diagnostico

paciente1 = Paciente("Andres","perro", "labrador", 5, 20.6)
consulta1= Consulta(paciente1,"17/2/23","Sintomas XXX","Cancer")
if __name__ == "__main__":
    print(paciente1.info_paciente())
    print(consulta1.info_consulta())