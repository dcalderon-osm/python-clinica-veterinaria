from Paciente import Paciente

class HistoriaClinica(Paciente):
    def __init__(self,paciente,fecha,diagnostico,tratamiento):
        super().__init__(paciente.nombre,paciente.especie, paciente.raza, paciente.edad, paciente.peso)
        self._fecha = fecha
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento

    def info_historia(self):
        return f"Fecha:[{self._fecha}],Diagnostico:[{self._diagnostico}],Tratamiento:[{self._tratamiento}]"


    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha


    @property
    def diagnostico(self):
        return self._diagnostico
    @diagnostico.setter
    def diagnostico(self,diagnostico):
        self._diagnostico = diagnostico


    @property
    def tratamiento(self):
        return self._tratamiento
    @tratamiento.setter
    def tratamiento(self,tratamiento):
        self._tratamiento = tratamiento

paciente1 = Paciente("Andres","perro", "labrador", 5, 20.6)
historia1 = HistoriaClinica(paciente1,"17/2/23", "Cancer", "Quimio")
if __name__ == "__main__":
    print(paciente1.info_paciente())
    print(historia1.info_historia())