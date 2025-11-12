from sqlalchemy.orm import Session
from database.connection import SessionLocal
from entities.usuario import Usuario
from entities.inventario import Inventario
from entities.juguete import Juguete
from utils.security import hash_password


def init_data():
    db: Session = SessionLocal()

    if db.query(Juguete).first():
        print("Datos ya inicializados.")
        db.close()
        return

    admin = Usuario(
        nombre="Admin", correo="admin@example.com", contrasena=hash_password("admin123")
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)

    juguetes_iniciales = [
        ("Electronico", "Robot", 100000, 5),
        ("Didactico", "Lego", 350000, 10),
        ("Coleccionable", "Funko", 60000, 3),
        ("Electronico", "Carro", 200000, 6),
        ("Didactico", "Rubik", 15000, 18),
        ("Coleccionable", "Goku", 97000, 2),
    ]
    for tipo, nombre, precio, stock in juguetes_iniciales:
        try:
            juguete = Juguete(
                nombre=nombre,
                precio=precio,
                stock=stock,
                tipo=tipo,
                usuario_id=admin.id,
            )
            db.add(juguete)
            db.flush()
            inventario = Inventario(
                juguete_id=juguete.id, usuario_id=admin.id, cantidad=stock
            )
            db.add(inventario)
        except Exception as e:
            print(f"Error al crear el juguete {nombre}: {e}")

    db.commit()
    print("Inventario predeterminado creado con éxito.")
    db.close()
