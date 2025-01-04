# Sistema de Gestión de Créditos

Este proyecto es un sistema básico de gestión de créditos desarrollado con Django. Permite manejar usuarios, créditos, pagos y garantías, e incluye una interfaz de usuario mejorada con Bootstrap.

## Características
- Gestión de usuarios: crear, editar, listar y eliminar usuarios.
- Gestión de créditos: crear, editar, listar y eliminar créditos.
- Gestión de pagos: registrar y listar pagos.
- Integración con Bootstrap para una interfaz moderna y responsiva.

## Requisitos
- Python 3.8+
- Django 4.0+
- Bootstrap (integrado a través de CDN en las plantillas HTML)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/jhoncarlosam-dev/sistema_credito.git
   cd sistema_credito
   ```

2. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

5. Accede a la aplicación en tu navegador:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura del Proyecto
```
sistema_credito/
├── sistema_credito/
│   ├── settings.py       # Configuración global
│   ├── urls.py           # Rutas principales
├── credito/
│   ├── models.py         # Modelos de la base de datos
│   ├── views.py          # Lógica de las vistas
│   ├── templates/        # Plantillas HTML
│   ├── forms.py          # Formularios
│   ├── urls.py           # Rutas específicas de la aplicación
├── db.sqlite3            # Base de datos SQLite
└── manage.py             # Herramienta CLI de Django
```

## Funcionalidades

### Gestión de Usuarios
- Crear un nuevo usuario.
- Editar información de un usuario existente.
- Eliminar usuarios.
- Listar todos los usuarios registrados.

### Gestión de Créditos
- Crear créditos asociados a usuarios.
- Editar y eliminar créditos.
- Listar créditos con detalles como monto, tasa de interés y estado.

### Gestión de Pagos
- Registrar pagos para créditos existentes.
- Ver el historial de pagos.

## Personalización
Puedes personalizar la configuración del sistema editando los archivos dentro de la carpeta `sistema_credito` y `credito`. Por ejemplo:
- Cambiar la base de datos en `settings.py`.
- Ajustar estilos en las plantillas HTML.

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar:
1. Haz un fork del proyecto.
2. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b nueva_funcionalidad
   ```
3. Realiza tus cambios y envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto
Para cualquier consulta o sugerencia, puedes contactarme en:
- **Correo**: jhoncarlosacevedomendoza@gmail.com
- **GitHub**: [https://github.com/jhoncarlosam-dev](https://github.com/jhoncarlosam-dev)
