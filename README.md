# Portafolio Personal - Eduardo Muñoz

Portfolio profesional construido con Django 5.x y PostgreSQL 17.

## Stack Tecnológico

- **Backend**: Django 5.x
- **Base de datos**: PostgreSQL 17
- **Frontend**: Bootstrap 4, jQuery (basado en plantilla Tunis)
- **Server**: Gunicorn
- **Contenedor**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Host**: VPS Contabo (173.249.63.138)

## Requisitos

- Python 3.12+
- Docker y Docker Compose
- PostgreSQL 17 (o usar el contenedor de Docker)

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/servicomf5/portafolio.git
cd portafolio
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

### 5. Crear base de datos

```bash
# En PostgreSQL
createdb portafolio_db
createuser portafolio_user
psql -c "GRANT ALL PRIVILEGES ON DATABASE portafolio_db TO portafolio_user;"
```

### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Ejecutar servidor

```bash
python manage.py runserver
```

## Instalación con Docker

### Desarrollo local

```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

El sitio estará disponible en: http://localhost:8012

### Producción (VPS)

El deploy se hace automáticamente via GitHub Actions cuando se push a `main`.

Para deploy manual:

```bash
ssh opencode@173.249.63.138
cd /opt/portafolio
docker-compose up -d --build
```

## Configuración del Admin

1. Acceder a http://localhost:8012/admin/
2. Crear/editar:
   - **Profile**: Información personal
   - **Skills**: Habilidades con porcentaje
   - **Experience**: Experiencia laboral y educación
   - **Projects**: Proyectos del portafolio
   - **Case Study**: Caso de estudio del bootcamp
   - **FODA Matrix**: Análisis FODA personal
   - **Company Research**: Investigación de empresa objetivo

## URLs

| Ruta | Descripción |
|------|-------------|
| `/` | Página de inicio (hero) |
| `/about/` | Sobre mí + Skills + FODA |
| `/portfolio/` | Proyectos + Caso de estudio |
| `/contact/` | Formulario de contacto |
| `/admin/` | Panel de administración Django |

## Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `DEBUG` | Modo debug | `True` |
| `SECRET_KEY` | Clave secreta Django | - |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
| `DB_NAME` | Nombre base de datos | `portafolio_db` |
| `DB_USER` | Usuario PostgreSQL | `portafolio_user` |
| `DB_PASSWORD` | Contraseña PostgreSQL | - |
| `DB_HOST` | Host PostgreSQL | `localhost` |
| `DB_PORT` | Puerto PostgreSQL | `5432` |
| `EMAIL_BACKEND` | Backend de email | `console.EmailBackend` |

## GitHub Secrets

Para el deploy automático necesitas configurar:

- `VPS_SSH_KEY`: Private SSH key para conectar al VPS
- `VPS_HOST`: IP del VPS (`173.249.63.138`)
- `VPS_USER`: Usuario SSH (`opencode`)
- `DJANGO_SECRET_KEY`: Secret key de Django
- `DB_PASSWORD`: Contraseña de la base de datos

## Estructura del Proyecto

```
portafolio/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── portafolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/         # App: Profile, Skills, Experience
├── projects/         # App: Projects, CaseStudy
├── content/          # App: FODA, CompanyResearch
├── contact/          # App: Contact Form
├── templates/        # Templates Django
├── static/           # CSS, JS, img, fonts
└── media/            # Archivos subidos
```

## Contacto

- **Email**: eduardomunoz.trabajo@gmail.com
- **LinkedIn**: https://linkedin.com/in/eduardomunozmunoz/
- **GitHub**: https://github.com/servicomf5
