import modules.corefiles as cf
import funciones.globales as gf
import funciones.Menuventa as fsp
import funciones.menucompras as fic
import main

<<<<<<< HEAD
def menuVenta(op: int):
    title = """
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
   ⚕️  🧑‍⚕️  MODULO ADMIN Ventas 👩‍⚕️  ⚕️
=======
<<<<<<< HEAD
def MenuVentas(op: int):
    title = """
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
   ⚕️  🧑‍⚕️  MODULO MENU COMPRAS  👩‍⚕️  ⚕️
=======
def menuVenta(op: int):
    title = """
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
   ⚕️  🧑‍⚕️  MODULO ADMIN Ventas 👩‍⚕️  ⚕️
>>>>>>> desarrollo
>>>>>>> main
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
    """
    menuVentaOp = '1. Agregar\n2. Editar\n3. ir a consulta\n4. eliminar\n5. Salir'
    gf.borrar_pantalla()
    if op != 5:  # Reemplazado 4 con 5 para salir en la opción 5
        print(title)
        print(menuVentaOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 6):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main

        match op:
            case 1:
                try:
                    fsp.Newventa()
                except Exception as e:
                    print("Error al agregar venta:", e)
                else:
                    print("venta agregado exitosamente")
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main

            case 2:
                try:
                    fsp.ModifyData()
                except Exception as e:
                    print("Error al editar venta:", e)
                else:
                    print("Datos de la venta editado exitosamente")
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main

            case 3:
                try:
                    fic.iraConsulta()
                except Exception as e:
                    print("Error al ir a consulta:", e)
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main

            case 4:
                try:
                    fsp.DeleteData()
                except Exception as e:
                    print("Error al eliminar especialista:", e)
                else:
                    print("Especialista eliminado exitosamente")
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main

            case 5:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
<<<<<<< HEAD
                menuVenta(0)
=======
<<<<<<< HEAD
                MenuVentas(0)
=======
                menuVenta(0)
>>>>>>> desarrollo
>>>>>>> main
