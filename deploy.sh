#!/bin/bash
# Deploy script para Portafolio Django

set -e

echo "=========================================="
echo "Deploying Portafolio Django"
echo "=========================================="

cd /opt/portafolio

echo "Deteniendo contenedores existentes..."
docker-compose down 2>/dev/null || true

echo "Construyendo e iniciando contenedores..."
docker-compose up -d --build

echo "Esperando que el contenedor esté listo..."
sleep 30

echo "Ejecutando migraciones..."
docker exec portafolio-web python manage.py migrate --noinput || echo "Sin migraciones pendientes"

echo "Recolectando archivos estáticos..."
docker exec portafolio-web python manage.py collectstatic --noinput || echo "Sin archivos estáticos"

echo "=========================================="
echo "¡Deploy completado!"
echo "Verifica en: http://173.249.63.138:8012"
echo "=========================================="
