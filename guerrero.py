from personaje import Personaje
from personaje import Fore, random

class Guerrero(Personaje):
    aumento_de_fuerza = 0
    aumento_de_def_fisica = 0
    def __init__(self, clase="Guerrero", nombre="Guerreritox", saludmax=150, manamax=0, fuerza=8, inteligencia=0, defensa_fisica=5, defensa_magica=2):
        super().__init__(nombre, clase, saludmax, manamax, fuerza, inteligencia, defensa_fisica, defensa_magica)

    def subir_nivel(self):
        super().subir_nivel()
        print(Fore.RED + f"Salud Maxima: {self.get_saludmax()} + 10 = {self.get_saludmax()+10}")
        self.set_saludmax(self.get_saludmax()+10)
        self.set_salud(self.get_saludmax())
        print(Fore.LIGHTRED_EX + f"Fuerza: {self.get_fuerza()} + 3 = {self.get_fuerza()+3}")
        self.set_fuerza(self.get_fuerza() + 3)
        print(Fore.LIGHTGREEN_EX + f"Defensa Fisica: {self.get_defensa_fisica()} + 3 = {self.get_defensa_fisica()+3}")
        self.set_def_fisica(self.get_defensa_fisica() + 3)
        print(Fore.LIGHTMAGENTA_EX + f"Defensa Magica: {self.get_defensa_magica()} + 1 = {self.get_defensa_magica()+1}")
        self.set_def_magica(self.get_defensa_magica() + 1)

    def grito_de_guerra(self):
        self.aumento_de_fuerza += 2
        self.aumento_de_def_fisica += 2
        print(Fore.GREEN + self.get_nombre() , "realiza", Fore.LIGHTBLUE_EX + "Grito de Guerra")
        print(Fore.LIGHTRED_EX + "Fuerza +2")
        print(Fore.LIGHTGREEN_EX + "Def. Fisica +2")

    def morir(self):
        super().morir()
        self.aumento_de_fuerza = 0
        self.aumento_de_def_fisica = 0