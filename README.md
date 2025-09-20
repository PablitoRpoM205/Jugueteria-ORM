# Sistema de Gestión de Juguetería ORM
Nuestro proyecto consiste en un Sistema de Gestión de Juguetería desarrollado en Python, una aplicación sencilla que Programación Orientada a Objetos para manejar diferentes tipos de juguetes con sus respectivas reglas de negocio con SQLAlchemy ORM para conectarse a PostgreSQL usando Neon como base de datos en la nube, incluyendo migraciones con Alembic y operaciones CRUD básicas.

## Descripción del Proyecto
Este proyecto implementa un sistema de inventario para una juguetería que permite gestionar tres tipos diferentes de juguetes:
- **Juguetes Electrónicos**: Con descuento máximo del 20%.
- **Juguetes Didácticos**: Con descuento máximo del 15%.
- **Juguetes Coleccionables**: Con descuento máximo del 4%
Cada tipo de juguete tiene sus propias reglas de descuento y hereda funcionalidades básicas de la clase padre `Juguete`.

## Características

- Gestión de usuarios con autenticación y roles (admin/usuario).
- CRUD de juguetes, con subtipos: electrónicos, didácticos y coleccionables.
- Inventario por usuario.
- Registro y consulta de ventas.
- Aplicación de descuentos según tipo de juguete.
- Interfaz de consola interactiva.
- Migraciones de base de datos con Alembic.

## Instalación

1. **Clona el repositorio y entra en la carpeta del proyecto**.

2. **Crea un entorno virtual e instálalo; con ello las dependencias:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. ¡Ejecuta el proyecto!:
   ```
   python main.py
   ```
4. **Navega por el menú**:
    1. Iniciar sesion
    2. Registrar usuario
    3. Mostrar inventario
    4. Vender juguete
    5. Aplicar descuento
    6. Ver ventas recientes
    7. Crear nuevo juguete
    8. Eliminar juguete
    9. Salir

## Uso del sistema
### Ejemplo de uso
**Opcion 1: Iniciar sesion**
```
Elige una opcion: 1
Nombre de usuario: admin
Contraseña: admin123
```
**Opcion 2: Registrar usuario**
```
Elige una opcion: 2
Nombre de usuario: administrador
Contraseña: (minimo 6 caracteres): admin2025
```
**Opcion 3: Mostrar inventario**
```
Elige una opción: 3
id | Carro | Precio: 200000.00 | Stock: 6 | Tipo: electronico
id | Funko | Precio: 60000.00 | Stock: 3 | Tipo: coleccionable
id | Goku | Precio: 97000.00 | Stock: 2 | Tipo: coleccionable
id | Lego | Precio: 350000.00 | Stock: 10 | Tipo: didactico
id | Robot | Precio: 100000.00 | Stock: 5 | Tipo: electronico
id | Rubik | Precio: 15000.00 | Stock: 18 | Tipo: didactico
```
**Opcion 4: Vender juguete**
```
Elige una opción: 4
Nombre o parte del nombre del juguete: lego
1. Lego (id:    ) - Precio: 350000.0 - Stock: 10 - Tipo: didactico
Cantidad a vender: 5
Venta registrada. ID venta: 
```
**Opcion 5: Aplicar descuento**
```
Elige una opción: 5
Nombre o parte del nombre del juguete: lego
1. Lego (id) - Precio: 350000.0 - Stock: 5 - Tipo: didactico
Porcentaje de descuento (entero): 25
Se aplicó el máximo de 15% para tipo didactico.
```
**Opcion 6: Ver ventas recientes**
```
Elige una opción: 6
id | Juguete: id_juguete | Cant: 5 | Total: 1750000.00 | Fecha: 2025-09-20 03:42:27.364963
```
**Opcion 7: Crear nuevo juguete**
```
Elige una opción: 7
Nombre del juguete: Buzz Lightyear
Precio: 80000
Stock inicial: 20
Tipo (electronico/didactico/coleccionable/otro): electronico
Juguete creado: Buzz Lightyear (id)
```
**Opcion 8: Eliminar juguete**
``` 
Elige una opción: 8
Nombre o parte del nombre del juguete: Buzz Lightyear 
1. Buzz Lightyear (id) - Precio: 40000.0 - Stock: 20 - Tipo: electronico
Juguete 'Barbie' eliminado correctamente.
```
**Opcion 9: Salir**
```
Elige una opción: 9
¡Gracias por utilizar nuestra aplicación!
```
## Estructura del proyecto

```
.
├── main.py
├── requirements.txt
├── .env
├── database/
│   ├── config.py
│   └── connection.py
├── entities/
│   ├── base.py
│   ├── usuario.py
│   ├── juguete.py
│   ├── inventario.py
│   ├── venta.py
│   ├── electronico.py
│   ├── didactico.py
│   └── coleccionable.py
├── crud/
│   ├── usuario_crud.py
│   ├── juguete_crud.py
│   └── venta_crud.py
├── auth/
│   └── auth.py
├── migrations/
│   └── ...
└── test_connection.py
```

## Autores
- Julián Esteban Álvarez Segura
- Juan Pablo Restrepo Muñoz

Instituto Tecnológico Metropolitano (ITM)





