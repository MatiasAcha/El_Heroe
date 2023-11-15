from personaje import Personaje
from personaje import Fore, random

class Mago(Personaje):
    def __init__(self, clase="Mago", nombre="Elfus", saludmax=100, manamax=100, fuerza=2, inteligencia=8, defensa_fisica=2, defensa_magica=8):
        super().__init__(nombre, clase, saludmax, manamax, fuerza, inteligencia, defensa_fisica, defensa_magica)

    def subir_nivel(self):
        super().subir_nivel()

        print(Fore.RED + f"Salud Maxima: {self.get_saludmax()} + 5 = {self.get_saludmax()+5}")
        self.set_saludmax(self.get_saludmax()+5)
        self.set_salud(self.get_saludmax())

        print(Fore.BLUE + f"Mana Maxima: {self.get_manamax()} + 25 = {self.get_manamax()+25}")
        self.set_manamax(self.get_manamax()+25)
        self.set_mana(self.get_manamax())

        print(Fore.LIGHTRED_EX + f"Fuerza: {self.get_fuerza()} + 1 = {self.get_fuerza()+1}")
        self.set_fuerza(self.get_fuerza() + 1)

        print(Fore.LIGHTBLUE_EX + f"Inteligencia: {self.get_inteligencia()} + 3 = {self.get_inteligencia()+3}")
        self.set_inteligencia(self.get_inteligencia() + 3)

        print(Fore.LIGHTGREEN_EX + f"Defensa Fisica: {self.get_defensa_fisica()} + 1 = {self.get_defensa_fisica()+1}")
        self.set_def_fisica(self.get_defensa_fisica() + 1)
        
        print(Fore.LIGHTMAGENTA_EX + f"Defensa Magica: {self.get_defensa_magica()} + 3 = {self.get_defensa_magica()+3}")
        self.set_def_magica(self.get_defensa_magica() + 3)

    def fuego(self, enemigo):
        if self.esta_vivo():
            if self.get_mana() >= 10:
                self.set_mana(self.get_mana() - 10)
                variacion = random.randint(-3, 3)
                daño = self.get_inteligencia() * 2 - enemigo.get_defensa_magica() + variacion + 7
                if daño < 0:
                    daño = 0
                enemigo.set_salud(enemigo.get_salud() - daño)
                print(Fore.GREEN + self.get_nombre(), "ha usado el hechizo", Fore.LIGHTRED_EX + "Fuego",
                      "contra", Fore.MAGENTA + enemigo.get_nombre(), Fore.RED + str(-daño), Fore.RED + "Salud")
                if enemigo.esta_vivo():
                    print(Fore.RED + "Salud", "restante de", Fore.MAGENTA + enemigo.get_nombre(), ":",
                          Fore.RED + str(enemigo.get_salud()), Fore.RED + "/", Fore.RED + str(enemigo.get_saludmax()))
                else:
                    enemigo.morir()
                    print(Fore.RED + enemigo.get_nombre(), Fore.RED + "ha muerto.")
            else:
                print(Fore.GREEN + self.get_nombre(), "no tiene mana suficiente.")

    def hielo(self, enemigo):
        if self.esta_vivo():
            if self.get_mana() >= 5:
                self.set_mana(self.get_mana() - 5)
                variacion = random.randint(-3, 3)
                daño = self.get_inteligencia() * 2 - enemigo.get_defensa_magica() + variacion + 4
                if daño < 0:
                    daño = 0
                enemigo.set_salud(enemigo.get_salud() - daño)
                print(Fore.GREEN + self.get_nombre(), "ha usado el hechizo", Fore.LIGHTBLUE_EX + "Hielo",
                      "contra", Fore.MAGENTA + enemigo.get_nombre(), Fore.RED + str(-daño), Fore.RED + "Salud")
                if enemigo.esta_vivo():
                    print(Fore.RED + "Salud", "restante de", Fore.MAGENTA + enemigo.get_nombre(), ":",
                          Fore.RED + str(enemigo.get_salud()), Fore.RED + "/", Fore.RED + str(enemigo.get_saludmax()))
                else:
                    enemigo.morir()
                    print(Fore.RED + enemigo.get_nombre(), Fore.RED + "ha muerto.")
            else:
                print(Fore.GREEN + self.get_nombre(), "no tiene mana suficiente.")

    def electro(self, enemigo):
        if self.esta_vivo():
            if self.get_mana() >= 15:
                self.set_mana(self.get_mana() - 15)
                variacion = random.randint(-3, 3)
                daño = self.get_inteligencia() * 2 - enemigo.get_defensa_magica() + variacion + 10
                if daño < 0:
                    daño = 0
                enemigo.set_salud(enemigo.get_salud() - daño)
                print(Fore.GREEN + self.get_nombre(), "ha usado el hechizo", Fore.YELLOW + "Electro",
                      "contra", Fore.MAGENTA + enemigo.get_nombre(), Fore.RED + str(-daño), Fore.RED + "Salud")
                if enemigo.esta_vivo():
                    print(Fore.RED + "Salud", "restante de", Fore.MAGENTA + enemigo.get_nombre(), ":",
                          Fore.RED + str(enemigo.get_salud()), Fore.RED + "/", Fore.RED + str(enemigo.get_saludmax()))
                else:
                    enemigo.morir()
                    print(Fore.RED + enemigo.get_nombre(), Fore.RED + "ha muerto.")
            else:
                print(Fore.GREEN + self.get_nombre(), "no tiene mana suficiente.")

    def cura(self, objetivo):
        if self.esta_vivo():
            if self.get_mana() >= 13:
                self.set_mana(self.get_mana() - 13)
                variacion = random.randint(-5, 3)
                curacion = self.get_inteligencia() * 2 + 5
                if curacion+objetivo.get_salud() > objetivo.get_saludmax():
                    curacion = objetivo.get_saludmax()-objetivo.get_salud()
                    objetivo.set_salud(objetivo.get_saludmax())   
                else:
                    objetivo.set_salud(objetivo.get_salud()+curacion)
                if self == objetivo:
                    print(Fore.GREEN + self.get_nombre(), "se ha curado por", Fore.GREEN + str(curacion),
                          Fore.GREEN + "Puntos de Salud")
                else:
                    print(Fore.GREEN + self.get_nombre(), "ha curado a", Fore.CYAN + objetivo.get_nombre(), "por",
                          Fore.GREEN + str(curacion), Fore.GREEN + "Puntos de Salud")
            else:
                print(Fore.GREEN + self.get_nombre(), "no tiene mana suficiente.")