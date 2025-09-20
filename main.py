from database.connection import SessionLocal, Base, engine
from entities.usuario import Usuario
from entities.electronico import Electronico
from entities.didactico import Didactico
from entities.coleccionable import Coleccionable
from entities.inventario import Inventario
from auth.auth import login_console, registrar_usuario_console
from crud.juguete_crud import (
    crear_juguete,
    obtener_juguetes,
    buscar_juguete_por_nombre,
    vender_juguete,
    aplicar_descuento,
    eliminar_juguete,
)
from crud.venta_crud import listar_ventas
from crud.usuario_crud import buscar_usuario_por_username, crear_usuario

Base.metadata.create_all(bind=engine)


def inicializar_demo(db, usuario_admin_id):
    if not obtener_juguetes(db):
        crear_juguete(db, "Robot", 100000.0, 5, "electronico", usuario_admin_id)
        crear_juguete(db, "Lego", 350000.0, 10, "didactico", usuario_admin_id)
        crear_juguete(db, "Funko", 60000.0, 3, "coleccionable", usuario_admin_id)
        crear_juguete(db, "Carro", 200000.0, 6, "electronico", usuario_admin_id)
        crear_juguete(db, "Rubik", 15000.0, 18, "didactico", usuario_admin_id)
        crear_juguete(db, "Goku", 97000.0, 2, "coleccionable", usuario_admin_id)


def mostrar_inventario(db):
    """
    Muestra el inventario completo en consola.
    """
    juguetes = obtener_juguetes(db)
    if not juguetes:
        print("Inventario vacío.")
        return
    for j in juguetes:
        print(
            f"{j.id} | {j.nombre} | Precio: {j.precio:.2f} | Stock: {j.stock} | Tipo: {j.tipo}"
        )


def seleccionar_juguete_por_nombre(db):
    """
    Pide nombre y devuelve la primer coincidencia.
    """
    nombre = input("Nombre o parte del nombre del juguete: ").strip()
    matches = buscar_juguete_por_nombre(db, nombre)
    if not matches:
        print("No se encontraron juguetes con ese nombre.")
        return None
    for idx, m in enumerate(matches, start=1):
        print(
            f"{idx}. {m.nombre} (id: {m.id}) - Precio: {m.precio} - Stock: {m.stock} - Tipo: {m.tipo}"
        )
    if len(matches) == 1:
        return matches[0]
    sel = input("Selecciona número: ").strip()
    if not sel.isdigit() or int(sel) < 1 or int(sel) > len(matches):
        print("Selección inválida.")
        return None
    return matches[int(sel) - 1]


def menu():
    """
    Loop principal del sistema. Requiere autenticación para acciones clave.
    """
    db = SessionLocal()
    admin = buscar_usuario_por_username(db, "admin")
    if not admin:
        admin = crear_usuario(db, "admin", "admin123", "admin")

    inicializar_demo(db, admin.id)

    usuario_activo = None

    while True:
        print("\n--- JUGUETERÍA (MENÚ) ---")
        if usuario_activo:
            print(f"Usuario: {usuario_activo.nombre} ({usuario_activo.correo})")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Mostrar inventario")
        print("4. Vender juguete")
        print("5. Aplicar descuento")
        print("6. Ver ventas recientes")
        print("7. Crear nuevo juguete")
        print("8. Eliminar juguete")
        print("9. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            usuario_activo = login_console(db)

        elif opcion == "2":
            usuario_activo = registrar_usuario_console(db)

        elif opcion == "3":
            mostrar_inventario(db)

        elif opcion == "4":
            if not usuario_activo:
                print("Debes iniciar sesión para vender.")
                continue
            juguete = seleccionar_juguete_por_nombre(db)
            if not juguete:
                continue
            entrada = input("Cantidad a vender: ").strip()
            if not entrada.isdigit():
                print("Ingresa un número válido.")
                continue
            cantidad = int(entrada)
            ok, res = vender_juguete(db, juguete.id, usuario_activo.id, cantidad)
            if ok:
                print(f"Venta registrada. ID venta: {res.id}")
            else:
                print(f"Error: {res}")

        elif opcion == "5":
            if not usuario_activo:
                print("Debes iniciar sesión para aplicar descuentos.")
                continue
            juguete = seleccionar_juguete_por_nombre(db)
            if not juguete:
                continue
            entrada = input("Porcentaje de descuento (entero): ").strip()
            if not entrada.lstrip("-").isdigit():
                print("Ingresa un número válido.")
                continue
            porcentaje = int(entrada)
            ok, mensaje = aplicar_descuento(
                db, juguete.id, porcentaje, actor_id=usuario_activo.id
            )
            print(mensaje)

        elif opcion == "6":
            ventas = listar_ventas(db)
            if not ventas:
                print("No hay ventas registradas.")
            else:
                for v in ventas:
                    print(
                        f"{v.id} | Juguete: {v.juguete_id} | Cant: {v.cantidad} | Total: {v.total:.2f} | Fecha: {v.fecha_venta}"
                    )

        elif opcion == "7":
            if not usuario_activo:
                print("Debes iniciar sesión para crear juguetes.")
                continue
            nombre = input("Nombre del juguete: ").strip()

            precio = input("Precio: ").strip()
            if precio == "" or not precio.replace(".", "", 1).isdigit():
                print("Precio inválido.")
                continue

            stock = input("Stock inicial: ").strip()
            if not stock.isdigit():
                print("Stock inválido. Debe ser un número entero.")
                continue

            tipo = input("Tipo (electronico/didactico/coleccionable/otro): ").strip()
            if tipo not in ["electronico", "didactico", "coleccionable", "otro"]:
                print("Tipo de juguete inválido.")
                continue

            try:
                precio_f = float(precio)
                stock_i = int(stock)
            except ValueError:
                print("Precio o stock inválido.")
                continue

            nuevo = crear_juguete(
                db, nombre, precio_f, stock_i, tipo, actor_id=usuario_activo.id
            )
            print(f"Juguete creado: {nuevo.nombre} (id: {nuevo.id})")

        elif opcion == "8":
            if not usuario_activo:
                print("Debes iniciar sesión para eliminar juguetes.")
                continue
            juguete = seleccionar_juguete_por_nombre(db)
            if not juguete:
                continue
            ok, mensaje = eliminar_juguete(db, juguete.id)
            print(mensaje)

        elif opcion == "9":
            print("¡Gracias por utilizar nuestra aplicación!")
            break

        else:
            print("Opción inválida.")

    db.close()


if __name__ == "__main__":
    menu()
