from mago import Mago
from guerrero import Guerrero

def main():
    # Aquí puedes crear instancias de tus clases y realizar operaciones
    # Ejemplo:
    maguito = Mago()
    guerrerito = Guerrero()

    # Realiza acciones con los personajes, como ataques o hechizos
    guerrerito.atacar(maguito)
    print("")
    maguito.fuego(guerrerito)
    print("")
    guerrerito.grito_de_guerra()
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.cura(maguito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.hielo(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.electro(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.electro(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.electro(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.electro(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    maguito.electro(guerrerito)
    print("")
    maguito.fuego(guerrerito)
    print("")
    guerrerito.atacar(maguito)
    print("")
    
    if maguito.esta_vivo():
        maguito.subir_nivel()
        print("")

    if guerrerito.esta_vivo():
        guerrerito.subir_nivel()
        print("")

    maguito.status()
    print("")
    guerrerito.status()

if __name__ == "__main__":
    main()
