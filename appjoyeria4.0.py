def precio_material(oro_bolsa:float) -> float:
    material:float = ((oro_bolsa * 0.91) + 4000) / (1.38)
    return material

def lista_precios(material:float, opciones:int):
    precio_productos = {
        "cadena nacional": 68000,
        "cadena italiana": 120000,
        "pulsera nacional": 68000,
        "pulsera italiana": 120000,
        "anillos": 68000,
        "herrajes": 68000,
        "dijes": 68000,
        "topos": 68000,
        "candongas":68000,
        "aretes": 68000,
        "balin liso": 53000,
        "balin diamantado": 58000
    }
    
    if opciones == 1: 
        precio_productos = {producto: precio + material for producto, precio in precio_productos.items()}
        for producto, precio in precio_productos.items():
            print(f"producto: {producto}, precio: {precio}")
        
    elif opciones == 2:
        precio_productos = {producto: precio + material - 12000 for producto, precio in precio_productos.items()}
        for producto, precio in precio_productos.items():
            print(f"producto: {producto}, precio: {precio}")
            
    elif opciones == 5:
        for producto in precio_productos:
            print(f"Producto: {producto}")
            
def facturar():
    venta_c:str = str(input("¿Se realizo la venta?: ")).lower()

    if venta_c == "si":
        nombre_c:str = str(input("Ingrese el nombre del cliente, nombre y apellido: "))
        cedula_c:str = str(input("Ingrese la cedula del cliente: "))
        celular_c:str = str(input("Ingrese el numero de celular del cliente: "))
        correo_c:str = str(input("Ingrese un correo electronico valido: "))
        efectivo_c:str = str(input("Ingrese el medio de pago utilizado: "))

        print("FACTURA DE VENTA: \n")
        print("Nombre del cliente: ",nombre_c)
        print("Cedula del cliente: ",cedula_c)
        print("Celular del cliente: ",celular_c)
        print("Correo electronico del cliente: ",correo_c)
        print("Metodo de pago utilizado: ", efectivo_c)
        print("-"*35)
        print("\n-----Factura-----")

    else:
        print("Es con mucho gusto")

def manejo_venta(oro_bolsa:float):
    
    material = precio_material(oro_bolsa)
    precio_productos = {
        "cadena nacional": 68000,
        "cadena italiana": 120000,
        "pulsera nacional": 68000,
        "pulsera italiana": 120000,
        "anillos": 68000,
        "herrajes": 68000,
        "dijes": 68000,
        "topos": 68000,
        "candongas":68000,
        "aretes": 68000,
        "balin liso": 53000,
        "balin diamantado": 58000
    }

    interruptor: bool = True
    
    while interruptor:

        print("""
            1) Lista de precios del día
            2) Lista de precios al por mayor
            3) Calcular precios productos y facturar
            4) Calcular venta al por mayor y facturar
            5) Productos disponibles
            6) Salir
            """)
        
        try:
            opciones: int = int(input("Ingrese una opción: "))

            if opciones == 6:
                print("Proceso finalizado")
                interruptor = False
            
            elif opciones in [1, 2]:
                lista_precios(material, opciones)
                
            elif opciones in [3, 4]:
                productos_seleccionados = []
                total_pagar: float = 0
                peso_contador: float = 0
                
                while True:
                        
                    producto: str = str(input("Ingrese el producto (o salir para finalizar): ")).lower()
                        
                    if producto == "salir":
                        print("")
                        break
                    
                    peso_producto: float = float(input("Ingrese el peso del artículo (en gramos): "))
                    
                    if producto in precio_productos:
                        peso_contador += peso_producto
                        
                        if opciones == 3:
                            precio = (precio_productos[producto] + material) * peso_producto
                            productos_seleccionados.append(producto)
                        
                        elif opciones == 4:
                            if peso_contador > 10:
                                precio = (precio_productos[producto] + material - 12000) * peso_producto
                                productos_seleccionados.append(producto)
                            else:
                                print("La venta al por mayor solo se podrá ejecutar para un peso mayor a 10 gramos")
                            
                        total_pagar += precio
                        print(f"El valor a pagar por {producto}g es: {round(precio)}$")
                       
                    else:
                        print("El producto no existe")
                        
                facturar()
                print("")
                print("Productos comprados: \n")
                for producto in productos_seleccionados:
                    print(producto)
                print(f"Total a pagar: {round(total_pagar)}\n")
                print("¡Muchas gracias por tu compra!")

            elif opciones == 5:
                lista_precios(material, 5)
                
            else:
                print("La opción no es válida")
        
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            
        #Imprime un mensaje que incluye la descripción del error ocurrido. El mensaje es útil para depurar problemas, ya que te permite ver el tipo de error y a veces una pista sobre qué salió mal.
        #Supongamos que hay un error en el código que no habías previsto, como una operación matemática que resulta en una excepción no anticipada. Si no tienes un bloque except genérico, 
        # el programa podría detenerse abruptamente al encontrar esa excepción. Con el bloque except Exception, el programa captura esa excepción y muestra un mensaje, lo que facilita la 
        # epuración y mejora la robustez del código.
        #En resumen, el último except actúa como una red de seguridad para capturar cualquier excepción no anticipada y proporcionar información útil sobre lo que salió mal, ayudando 
        # en la depuración y manteniendo el programa en funcionamiento de manera más confiable.
        
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

oro_bolsa: float = float(input("Ingrese el valor del oro en bolsa o en la app Gold Price: "))

manejo_venta(oro_bolsa)