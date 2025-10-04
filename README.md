# Sistema de Gestión de Juguetería API
Nuestro proyecto consiste en un Sistema de Gestión de Juguetería desarrollado en Python, ahora transformado en una API RESTful utilizando FastAPI. Esta aplicación permite manejar diferentes tipos de juguetes con sus respectivas reglas de negocio, conectándose a PostgreSQL usando Neon como base de datos en la nube, incluyendo migraciones con Alembic y operaciones CRUD básicas.

## Descripción del Proyecto
Este proyecto implementa un sistema de inventario para una juguetería que permite gestionar tres tipos diferentes de juguetes:
- **Juguetes Electrónicos**: Con descuento máximo del 20%.
- **Juguetes Didácticos**: Con descuento máximo del 15%.
- **Juguetes Coleccionables**: Con descuento máximo del 4%.

Cada tipo de juguete tiene sus propias reglas de descuento y hereda funcionalidades básicas de la clase padre `Juguete`.

## Características

- Gestión de usuarios con autenticación y roles (admin/usuario).
- CRUD de juguetes, con subtipos: electrónicos, didácticos y coleccionables.
- Inventario por usuario.
- Registro y consulta de ventas.
- Aplicación de descuentos según tipo de juguete.
- API RESTful con endpoints para cada entidad.
- Migraciones de base de datos con Alembic.

## Instalación

1. **Clona el repositorio y entra en la carpeta del proyecto**.

2. **Crea un entorno virtual e instálalo; con ello las dependencias:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Ejecuta el servidor de la API**:
   ```sh
   uvicorn main:app --reload
   ```

## Uso de la API

### Endpoints

- **Usuarios**
  - `POST /usuarios`: Crear un nuevo usuario.
  - `GET /usuarios`: Obtener todos los usuarios.
  - `GET /usuarios/{id}`: Obtener un usuario por ID.
  - `PUT /usuarios/{id}`: Actualizar un usuario por ID.
  - `DELETE /usuarios/{id}`: Eliminar un usuario por ID.

- **Juguetes**
  - `POST /juguetes`: Crear un nuevo juguete.
  - `GET /juguetes`: Obtener todos los juguetes.
  - `GET /juguetes/{id}`: Obtener un juguete por ID.
  - `PUT /juguetes/{id}`: Actualizar un juguete por ID.
  - `DELETE /juguetes/{id}`: Eliminar un juguete por ID.

- **Ventas**
  - `POST /ventas`: Crear una nueva venta.
  - `GET /ventas`: Obtener todas las ventas.
  - `GET /ventas/{id}`: Obtener una venta por ID.
  - `PUT /ventas/{id}`: Actualizar una venta por ID.
  - `DELETE /ventas/{id}`: Eliminar una venta por ID.

- **Inventario**
  - `GET /inventario`: Obtener el inventario.
  - `PUT /inventario`: Actualizar el inventario.

- **Autenticación**
  - `POST /auth/login`: Iniciar sesión.
  - `POST /auth/register`: Registrar un nuevo usuario.

## Estructura del proyecto

```
.
├── api/
│   ├── __init__.py
│   ├── usuario.py
│   ├── juguete.py
│   ├── venta.py
│   ├── inventario.py
│   └── auth.py
├── auth/
│   └── auth.py
├── crud/
│   ├── usuario_crud.py
│   ├── juguete_crud.py
│   └── venta_crud.py
├── database/
│   ├── __init__.py
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
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 04c005510a3f_add_authentication_fields_to_usuarios_.py
├── main.py
├── requirements.txt
├── test_connection.py
├── .env
├── .gitignore
├── alembic.ini
└── README.md
```

## Autores
- Julián Esteban Álvarez Segura
- Juan Pablo Restrepo Muñoz

Instituto Tecnológico Metropolitano (ITM)