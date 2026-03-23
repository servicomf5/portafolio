# Portafolio Personal - Django Portfolio

Proyecto académico de portafolio profesional construido con Django 5.x y PostgreSQL. Este proyecto cumple con los requisitos del Bootcamp de Python, demostrando proficiency en:

- Desarrollo web con Django
- Base de datos PostgreSQL
- Docker y despliegue
- Git y control de versiones

## Stack Tecnológico

- **Backend**: Django 5.x (Python 3.x)
- **Base de datos**: PostgreSQL 17
- **Frontend**: Bootstrap 4, jQuery (basado en plantilla Tunis)
- **Contenedor**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Deployment**: VPS (Contabo)

## Características

- ✅ Perfil profesional dinámicas desde Base de Datos
- ✅ Sistema de habilidades con porcentajes visuales
- ✅ Gestión de experiencia laboral y educación
- ✅ Portafolio de proyectos con imágenes
- ✅ Caso de estudio del bootcamp
- ✅ Análisis FODA personal
- ✅ Investigación de empresa objetivo
- ✅ Formulario de contacto funcional
- ✅ Panel de administración Django
- ✅ Diseño responsivo (Bootstrap 4)
- ✅ plantilles Multilenguaje (Español)

## Requisitos

- Python 3.11+
- PostgreSQL 17 (o contenedor Docker)

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/servicomf5/portafolio.git
cd portafolio
```

### 2. Crear entorno virtual

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

El proyecto incluye un archivo `.env.example`. Copiar y configurar:

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar con tus configuraciones (solo modificar si es necesario)
# Los valores por defecto funcionan para desarrollo local
```

### 5. Crear base de datos PostgreSQL

```bash
# Acceder a PostgreSQL
psql -U postgres

# Ejecutar en la terminal de PostgreSQL:
CREATE DATABASE portafolio_db;
CREATE USER portafolio_user WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE portafolio_db TO portafolio_user;
\q
```

### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

### 7. (Opcional) Cargar datos de ejemplo

El proyecto incluye fixtures con datos de ejemplo para testing:

```bash
python manage.py loaddata portfolio/fixtures/skills
python manage.py loaddata portfolio/fixtures/experiences
python manage.py loaddata projects/fixtures/projects
python manage.py loaddata projects/fixtures/casestudy
python manage.py loaddata content/fixtures/foda
python manage.py loaddata content/fixtures/company
```

**Nota**: Las imágenes (foto de perfil, CV, imágenes de proyectos) deben subirse desde el panel de administración Django.

### 8. Crear superusuario

```bash
python manage.py createsuperuser
```

### 9. Ejecutar servidor

```bash
python manage.py runserver
```

El sitio estará disponible en: http://127.0.0.1:8000/

## Instalación con Docker

### Desarrollo local

```bash
# Construir y levantar contenedores
docker-compose up -d

# Ejecutar migraciones
docker-compose exec web python manage.py migrate

# Crear superusuario
docker-compose exec web python manage.py createsuperuser
```

El sitio estará disponible en: http://localhost:8012

### Producción (VPS)

El deploy se realiza automáticamente via GitHub Actions al hacer push a `main`.

Para deploy manual:

```bash
ssh root@<tu-vps>
cd /opt/portafolio
docker-compose up -d --build
```

## URLs del Proyecto

| Ruta | Descripción |
|------|-------------|
| `/` | Página de inicio (hero) |
| `/about/` | Sobre mí, Skills, Experiencia, FODA |
| `/portfolio/` | Proyectos y Caso de estudio |
| `/contact/` | Formulario de contacto |
| `/admin/` | Panel de administración Django |

## Panel de Administración

Acceder a `/admin/` con el superusuario creado. Desde allí se pueden gestionar:

- **Profile**: Información personal, foto, CV
- **Skills**: Habilidades técnicas y blandas
- **Experience**: Experiencia laboral y educación
- **Projects**: Proyectos del portafolio
- **Case Study**: Caso de estudio del bootcamp
- **FODA Matrix**: Análisis FODA
- **Company Research**: Investigación empresa objetivo

## Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `DEBUG` | Modo debug | `True` |
| `DJANGO_SECRET_KEY` | Clave secreta Django | (generar nueva) |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
| `DB_NAME` | Nombre base de datos | `portafolio_db` |
| `DB_USER` | Usuario PostgreSQL | `portafolio_user` |
| `DB_PASSWORD` | Contraseña PostgreSQL | (configurar) |
| `DB_HOST` | Host PostgreSQL | `localhost` |
| `DB_PORT` | Puerto PostgreSQL | `5432` |
| `EMAIL_BACKEND` | Backend de email | `console.EmailBackend` |
| `EMAIL_HOST` | Servidor SMTP | `smtp.gmail.com` |
| `EMAIL_PORT` | Puerto SMTP | `587` |
| `CONTACT_EMAIL` | Email de destino del contacto | `email@ejemplo.com` |

## GitHub Actions (CI/CD)

El proyecto incluye workflow de GitHub Actions para deploy automático:

1. Push a rama `main` dispara el workflow
2. Se conecta al VPS por SSH
3. Sube archivos, rebuild Docker
4. Ejecuta migraciones y collectstatic

### Secrets requeridos en GitHub:

- `VPS_SSH_KEY`: Clave privada SSH
- `VPS_HOST`: IP del VPS
- `VPS_USER`: Usuario SSH
- `DJANGO_SECRET_KEY`: Secret key de Django
- `DB_PASSWORD`: Contraseña PostgreSQL
- `EMAIL_PASSWORD`: Password SMTP (opcional)

## Estructura del Proyecto

```
portafolio/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── portafolio/          # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/           # App: Perfil, Skills, Experiencia
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── fixtures/
├── projects/           # App: Proyectos, CaseStudy
│   ├── models.py
│   ├── views.py
│   └── fixtures/
├── content/           # App: FODA, CompanyResearch
│   ├── models.py
│   └── fixtures/
├── contact/           # App: Formulario contacto
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/         # Templates HTML
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   └── portfolio/
├── static/            # CSS, JS, imágenes
└── media/              # Archivos subidos (perfil, proyectos)
```

## Buenas Prácticas Incluidas

- Código en inglés
- Comentarios en español
- Separación de responsabilidades (MTV pattern)
- Variables de entorno para configuración
- Manejo de errores apropiado
- Migraciones para base de datos
- Fixtures para datos de ejemplo

## Licencia

Este proyecto es de uso académico y profesional.

---

**Nota**: Este proyecto fue desarrollado como parte del Bootcamp de Python. Los datos de ejemplo en los fixtures son genéricos y deben ser reemplazados con información real desde el panel de administración.