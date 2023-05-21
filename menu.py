#librerias de uso
from Inventario import Inventario
#---------------MENU------------------
def menu():
    #ruta del archivo de base datos
    url_database = "datos.txt"
    inventario = Inventario(url_database)
    menu = '''
        \n################# MENU ###################
        1. Adquirir producto
        2. Vender producto
        3. Mostrar productos existentes
        4. Mostrar ventas realizadas
        5. Salir\n#########################################\n
    '''
    opc = "0"
    while (opc != "5"):
        print("\n",menu, "\n")
        opc = input("Ingrese una opción: ")

        if (opc == "1"):
            print("Adquirir un nuevo producto: \n")
            inventario.adquirir_producto()
        elif (opc == "2"):
            print("Vender productos")
            inventario.vender_producto()
        elif (opc == "3"):
            print("Inventario de productos: ")
            inventario.mostrar_productos()
        elif (opc == "4"):
            print("Inventarios de ventas: ")
            inventario.mostrar_ventas()
            print()
        elif (opc == "5"):
            print("\nGracias por usar el sistema de invetarios\n")
        else:
            print("\nOpcion no existente, por favor ingrese una opcion del menu.\n")

menu()
