# Sistema de Gestión de Juguetería Frontend

Este proyecto es una aplicación frontend desarrollada con **Angular** para interactuar con la API de gestión de juguetería. Permite a los usuarios gestionar usuarios, juguetes, ventas e inventario a través de una interfaz amigable.

## Descripción

La aplicación proporciona una serie de componentes y servicios que permiten realizar operaciones CRUD sobre los recursos disponibles en la API. Los usuarios pueden iniciar sesión, gestionar su inventario, y realizar ventas de juguetes.

## Características

- Interfaz de usuario intuitiva y responsiva.
- Autenticación de usuarios.
- Gestión de usuarios, juguetes, ventas e inventario.
- Integración con la API RESTful de gestión de juguetería.
- Rutas protegidas para funcionalidades que requieren autenticación.

## Instalación

1. **Clona el repositorio y entra en la carpeta del proyecto:**
   ```sh
   git clone <url-del-repo>
   cd jugueteria-frontend
   ```

2. **Instala las dependencias:**
   ```sh
   npm install
   ```

3. **Ejecuta la aplicación:**
   ```sh
   ng serve
   ```

4. **Abre tu navegador y visita:**
   ```
   http://localhost:4200
   ```

## Estructura del Proyecto

```
jugueteria-frontend
├── e2e
│   ├── src
│   │   └── app.e2e-spec.ts
│   └── protractor.conf.js
├── src
│   ├── app
│   │   ├── core
│   │   │   ├── services
│   │   │   │   ├── auth.service.ts
│   │   │   │   ├── usuarios.service.ts
│   │   │   │   ├── juguetes.service.ts
│   │   │   │   ├── ventas.service.ts
│   │   │   │   └── inventario.service.ts
│   │   │   ├── guards
│   │   │   │   └── auth.guard.ts
│   │   │   └── interceptors
│   │   │       └── auth.interceptor.ts
│   │   ├── models
│   │   │   ├── usuario.model.ts
│   │   │   ├── juguete.model.ts
│   │   │   ├── venta.model.ts
│   │   │   └── inventario.model.ts
│   │   ├── components
│   │   │   ├── auth
│   │   │   │   └── login
│   │   │   │       └── login.component.ts
│   │   │   ├── usuarios
│   │   │   │   └── usuarios.component.ts
│   │   │   ├── juguetes
│   │   │   │   └── juguetes.component.ts
│   │   │   ├── ventas
│   │   │   │   └── ventas.component.ts
│   │   │   └── inventario
│   │   │       └── inventario.component.ts
│   │   ├── pages
│   │   │   └── dashboard
│   │   │       └── dashboard.component.ts
│   │   ├── app-routing.module.ts
│   │   └── app.module.ts
│   ├── assets
│   │   └── styles
│   │       └── _variables.scss
│   ├── environments
│   │   ├── environment.ts
│   │   └── environment.prod.ts
│   ├── index.html
│   ├── main.ts
│   ├── polyfills.ts
│   ├── styles.scss
│   └── test.ts
├── angular.json
├── package.json
├── tsconfig.json
├── tsconfig.app.json
├── tsconfig.spec.json
├── karma.conf.js
├── .eslintrc.json
├── .editorconfig
├── .gitignore
└── README.md
```

¡Gracias por tu interés en el proyecto!