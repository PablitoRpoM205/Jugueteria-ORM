# Sistema de Gestión de Juguetería API

Este proyecto es una API RESTful desarrollada con **FastAPI** para la gestión de una juguetería. Permite administrar usuarios, inventario, ventas y diferentes tipos de juguetes, aplicando reglas de negocio específicas para cada tipo. Utiliza **PostgreSQL** (Neon en la nube), migraciones con **Alembic** y operaciones CRUD completas.

## Descripción

El sistema gestiona tres tipos de juguetes, cada uno con su propio límite de descuento:
- **Electrónicos**: hasta 20%
- **Didácticos**: hasta 15%
- **Coleccionables**: hasta 4%

Cada tipo hereda de la clase base `Juguete` y tiene reglas de negocio particulares.

## Características

- Autenticación y roles (admin/usuario)
- CRUD de usuarios, juguetes, ventas e inventario
- Inventario por usuario
- Registro y consulta de ventas
- Aplicación de descuentos según tipo de juguete
- Migraciones con Alembic
- API RESTful modularizada por entidad

## Instalación

1. **Clona el repositorio y entra en la carpeta del proyecto:**
   ```sh
   git clone <url-del-repo>
   cd Jugueteria-ORM
   ```

2. **Crea un entorno virtual e instala las dependencias:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configura la base de datos en el archivo `.env`**  
   (ya incluido en el proyecto, revisa la variable `DATABASE_URL`).

4. **Ejecuta el servidor de la API:**
   ```sh
   uvicorn main:app --reload
   ```

## Uso de la API

### Endpoints principales

- **Usuarios**
  - `POST /usuarios` — Crear usuario
  - `GET /usuarios` — Listar usuarios
  - `GET /usuarios/{id}` — Obtener usuario por ID
  - `PUT /usuarios/{id}` — Actualizar usuario
  - `DELETE /usuarios/{id}` — Eliminar usuario

- **Juguetes**
  - `POST /juguetes` — Crear juguete
  - `GET /juguetes` — Listar juguetes
  - `GET /juguetes/{id}` — Obtener juguete por ID
  - `PUT /juguetes/{id}` — Actualizar juguete
  - `DELETE /juguetes/{id}` — Eliminar juguete

- **Ventas**
  - `POST /ventas` — Registrar venta
  - `GET /ventas` — Listar ventas
  - `GET /ventas/{id}` — Obtener venta por ID
  - `PUT /ventas/{id}` — Actualizar venta
  - `DELETE /ventas/{id}` — Eliminar venta

- **Inventario**
  - `GET /inventario` — Consultar inventario
  - `PUT /inventario` — Actualizar inventario

- **Autenticación**
  - `POST /auth/login` — Iniciar sesión
  - `POST /auth/register` — Registrar usuario

## Estructura del Proyecto

```
.
├── api/
│   ├── auth.py
│   ├── dependencias.py
│   ├── inventario.py
│   ├── juguete.py
│   ├── usuario.py
│   └── venta.py
├── auth/
│   └── auth.py
├── crud/
│   ├── inventario_crud.py
│   ├── juguete_crud.py
│   ├── usuario_crud.py
│   └── venta_crud.py
├── database/
│   ├── config.py
│   └── connection.py
├── entities/
│   ├── base.py
│   ├── coleccionable.py
│   ├── didactico.py
│   ├── electronico.py
│   ├── inventario.py
│   ├── juguete.py
│   ├── usuario.py
│   └── venta.py
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── schemas/
│   ├── inventario.py
│   ├── juguete.py
│   ├── usuario.py
│   └── venta.py
├── utils/
│   ├── exceptions.py
│   └── security.py
├── main.py
├── init_db.py
├── requirements.txt
├── .env
├── alembic.ini
├── test_connection.py
└── README.md
```

¡Muchas gracias!

## Autores

- Julián Esteban Álvarez Segura
- Juan Pablo Restrepo Muñoz

Instituto Tecnológico Metropolitano (ITM)
