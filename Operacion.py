from Paciente import Paciente


class Operacion(Paciente):
    def __init__(self, paciente, fecha, tipo, diagnostico):
        super().__init__(paciente.nombre,paciente.especie, paciente.raza, paciente.edad, paciente.peso)
        self._fecha = fecha
        self._tipo = tipo
        self._diagnostico = diagnostico

    def info_operacion(self):
        return f"Fecha de la operacion:[{self._fecha}],tipo de la operacion:[{self._tipo}],Diagnostico de la operacion:[{self._diagnostico}]"

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def diagnostico(self):
        return self._diagnostico

    @diagnostico.setter
    def diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

paciente1 = Paciente("Andres","perro", "labrador", 5, 20.6)
operacion1=Operacion(paciente1,"17/2/23","Cirugia","Exitoso")
if __name__=="__main__":
    print(paciente1.info_paciente())
    print(operacion1.info_operacion())