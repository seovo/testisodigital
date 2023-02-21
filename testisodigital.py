Productos = ['Pantalones', 'Camisas', 'Corbatas', 'Casacas']
Precios = [200.00, 120.00, 50.00, 350.00]
Stock = [50, 45, 30,15]

print("====================")
print("LISTA DE PRODUCTOS")
print("====================")



from tabulate import tabulate

def shw_table():
    cola = []
    c = 0

    for prod in Productos:
        cola.append([c +1 ,Productos[c], Precios[c], Stock[c]])
        c += 1

    print(tabulate(cola, headers=['#','Producto', 'Precio', 'Stock']))
    print('______')
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir .")
    code = str(input())
    print(code)
    if code == '4':
        exit()
    if code == '1':
        print("INGRESE EL NOMBRE DEL PRODUCTO ")
        producto = str(input())
        print("INGRESE PRECIO")
        precio =  float(input())
        print("INGRESE STOCK")
        stock = int(input())

        Productos.append(producto)
        Precios.append(precio)
        Stock.append(stock)
        shw_table()

    if code == '2':
        print('INGRESE EL NUMERO DE ORDEN # A ELIMINAR')
        deletex = int(input())
        del Productos[deletex - 1]
        del Precios[deletex - 1]
        del Stock[deletex - 1]
        shw_table()

    if code == '3':
        print('INGRESE EL NUMERO DE ORDEN # A ACTUALIZAR')
        orden = int(input()) - 1
        print('DESEA ACTUALIZAR EL NOMBRE ? Y/N')
        yn = str(input())
        if yn.find('Y') != -1 or yn.find('y') != -1:
            print("INGRESE EL NOMBRE DEL PRODUCTO ")
            producto = str(input())
            Productos[orden] = producto


        print('DESEA ACTUALIZAR EL PRECIO ? Y/N')
        yn = str(input())
        if yn.find('Y') != -1 or yn.find('y') != -1:
            print("INGRESE EL PRECIO ")
            producto = float(input())
            Precios[orden] = producto

        print('DESEA ACTUALIZAR EL STOCK ? Y/N')
        yn = str(input())
        if yn.find('Y') != -1 or yn.find('y') != -1:
            print("INGRESE EL STOCK ")
            producto = int(input())
            Stock[orden] = producto

        shw_table()




shw_table()





#print([cola,colb,colc])
