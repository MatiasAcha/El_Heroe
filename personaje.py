import random
from colorama import init, Fore

init(autoreset=True)

class Personaje:
    def __init__(self, nombre, clase, saludmax, manamax, fuerza, inteligencia, defensa_fisica, defensa_magica):
        self.__nombre = nombre
        self.__clase = clase
        self.__salud = saludmax
        self.__saludmax = saludmax
        self.__mana = manamax
        self.__manamax = manamax
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa_fisica = defensa_fisica
        self.__defensa_magica = defensa_magica
        self.__nivel = 1
    
    def status(self):
        print("Nombre:", self.get_nombre())
        print(Fore.GREEN + "Nivel:", Fore.GREEN + str(self.get_nivel()))
        print(Fore.RED + "-Salud:", Fore.RED + str(self.get_salud()), Fore.RED + "/", Fore.RED + str(self.get_saludmax()))
        print(Fore.BLUE + "-Mana:", Fore.BLUE + str(self.get_mana()), Fore.BLUE + "/", Fore.BLUE + str(self.get_manamax()))
        print(Fore.LIGHTRED_EX +"-Fuerza:", Fore.LIGHTRED_EX + str(self.get_fuerza()))
        print(Fore.LIGHTBLUE_EX + "-Inteligencia:", Fore.LIGHTBLUE_EX + str(self.get_inteligencia()))
        print(Fore.LIGHTGREEN_EX + "-Def fisica:", Fore.LIGHTGREEN_EX + str(self.get_defensa_fisica()))
        print(Fore.LIGHTMAGENTA_EX + "-Def magica:", Fore.LIGHTMAGENTA_EX + str(self.get_defensa_magica()))

    def esta_vivo(self):
        return self.__salud > 0

    def morir(self):
        self.__salud = 0

    def subir_nivel(self):
        self.__nivel += 1
        print(Fore.YELLOW + f"¡{self.get_nombre()} ha subido de nivel! Nuevo nivel: {self.get_nivel()}")


    def atacar(self, enemigo):
        if self.esta_vivo():
            variacion = random.randint(-3, 3)
            critico = random.randint(1, 10)
            danio = 0
            #Calcula el daño que hacemos segun nuestra clase
            if self.__clase =="Guerrero":
                danio = ((self.get_fuerza() + self.aumento_de_fuerza) * 2 + variacion)
            else:
                danio = (self.get_fuerza() * 2 + variacion)
            #Calcula el daño que se reduce segun la clase del enemigo
            if enemigo.__clase == "Guerrero":
                danio = danio - enemigo.get_defensa_fisica() - enemigo.aumento_de_def_fisica
            else:
                danio = danio - enemigo.get_defensa_fisica()
            #Verifica si se realiza un Critico. De ser asi el daño calculado pasa a ser el doble.
            if critico == 10:
                danio = danio * 2
            #Verifica si se realiza es menor a 0. De ser así el daño es 0.
            if danio < 0:
                danio = 0
            #Aplica el daño.
            enemigo.set_salud(enemigo.get_salud() - danio)
            #Muestra el mensaje del ataque y la salud con la que queda el enemigo.
            if critico == 10 and danio > 0:
                print(Fore.GREEN + self.get_nombre(), "ha atacado a", Fore.MAGENTA + enemigo.get_nombre(),
                      Fore.RED + str(-danio), Fore.RED + "Salud ¡CRITICO!")
            else:
                print(Fore.GREEN + self.get_nombre(), "ha atacado a", Fore.MAGENTA + enemigo.get_nombre(),
                      Fore.RED + str(-danio), Fore.RED + "Salud")

            if enemigo.esta_vivo():
                print(Fore.RED + "Salud", "restante de", Fore.MAGENTA + enemigo.get_nombre(), ":",
                      Fore.RED + str(enemigo.get_salud()), Fore.RED + "/", Fore.RED + str(enemigo.get_saludmax()))
            else:
                enemigo.morir()
                print(Fore.RED + enemigo.get_nombre(), Fore.RED + "ha muerto.")

    # Setters
    def set_salud(self, nueva_salud):
        self.__salud = nueva_salud

    def set_mana(self, nuevo_mana):
        self.__mana = nuevo_mana

    def set_saludmax(self, nueva_saludmax):
        self.__saludmax = nueva_saludmax

    def set_manamax(self, nueva_manamax):
        self.__manamax = nueva_manamax    

    def set_fuerza(self, nueva_fuerza):
        self.__fuerza = max(0, nueva_fuerza)

    def set_inteligencia(self, nueva_inteligencia):
        self.__inteligencia = max(0, nueva_inteligencia)

    def set_def_fisica(self, nueva_def_fisica):
        self.__defensa_fisica = max(0, nueva_def_fisica)

    def set_def_magica(self, nueva_def_magica):
        self.__defensa_magica = max(0, nueva_def_magica)

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_fuerza(self):
        return self.__fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_defensa_fisica(self):
        return self.__defensa_fisica

    def get_defensa_magica(self):
        return self.__defensa_magica

    def get_salud(self):
        return self.__salud

    def get_saludmax(self):
        return self.__saludmax

    def get_mana(self):
        return self.__mana

    def get_manamax(self):
        return self.__manamax

    def get_nivel(self):
        return self.__nivel
