class Paciente:
    def __init__(self,nombre,especie,raza,edad,peso):
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._peso = peso

    def info_paciente(self):
        return f"Nombre:[{self._nombre}],Especie:[{self._especie}],Raza:[{self._raza}],Edad:[{self._edad}],Peso:[{self._peso}Kg]"


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre


    @property
    def especie(self):
        return self._especie
    @especie.setter
    def especie(self, especie):
        self._especie = especie


    @property
    def raza(self):
        return self._raza
    @raza.setter
    def raza(self, raza):
        self._raza = raza


    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad


    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self,peso):
        self._peso = peso


paciente1= Paciente ("Mario" ,"Perro","Pitbull",12,34.57)
# paciente2= Paciente ("Andrea","Gato","Montes",20,56.4)
# paciente3= Paciente ("Luis","Perro","Chihuaha",8,25.45)

# print(paciente1.info_paciente())
# print(paciente2.info_paciente())
# print(paciente3.info_paciente())

if __name__ == "__main__":
    print(paciente1.info_paciente())