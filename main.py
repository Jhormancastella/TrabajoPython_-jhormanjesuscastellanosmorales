import modules.corefiles as cf
import modules.corefilesP as cfp
import funciones.globales as fg
import ui.uiMenuventa as uiSp
import ui.uiMenucompras as uiPt
import ui.uiMenuRegistro as uiC

def mainMenu(op):
    fg.borrar_pantalla()
    title = """
    🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯
    🥖 👩🏻‍🍳👩🏻‍🍳👩🏻‍🍳👩🏻‍🍳👩🏻‍🍳 PanCamp 👩🏽‍🍳👩🏽‍🍳👩🏽‍🍳👩🏽‍🍳👩🏽‍🍳 🥖
    🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯🥐🥨🥪🥯🥖🍞🥐🥨🥪🥯
    """
    mainMenuOp = "1. Menu venta\n2. Menu Compras\n3. Menu Registro\n4. Salir"
    if op != 4:
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('Error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            if opcion == 1:
<<<<<<< HEAD
                uiSp.MenuVentas(0)
=======
                uiSp.menuVenta(0)
>>>>>>> desarrollo
            elif opcion == 2:
                uiPt.MenuCompras(0)
            elif opcion == 3:
                uiC.MenuRegistro(0)
            elif opcion == 4:
                print("Regrese pronto ....")
                fg.pausar_pantalla()
            else:
                print('Opcion ingresada no pertenece al menu de opciones')
                fg.pausar_pantalla()
                mainMenu(0)

if __name__ == '__main__':
    cf.MY_DATABASE = 'data/venta.json'
    cfp.MY_DATABASEP = 'data/compras.json'
    cf.checkFile(fg.centroClinico)
    cfp.checkFile(fg.centroClinico)
    mainMenu(0)
