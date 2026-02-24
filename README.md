# Invitación de Boda Digital

Esta es una aplicación web construida con Flask para una tarjeta de invitación de boda digital interactiva.

## Características

*   **Sobre animado:** Apertura interactiva con sello 3D.
*   **Cuenta regresiva:** Tiempo restante para el evento.
*   **Itinerario:** Cronograma de actividades.
*   **Galería de fotos:** Carrusel de imágenes dinámico.
*   **Música de fondo:** Reproductor de audio con control de volumen.
*   **Ubicación:** Enlaces directos a Google Maps.
*   **Datos dinámicos:** Toda la información se carga desde `boda_data.json`.

## Instalación Local

1.  Clonar el repositorio.
2.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecutar la aplicación:
    ```bash
    python tarjeta.py
    ```
4.  Abrir en el navegador: `http://localhost:5000`

## Despliegue

Este proyecto está configurado para desplegarse fácilmente en plataformas como **Render**, **Vercel** o **Heroku**.

*   Se incluye un archivo `Procfile` para el uso de Gunicorn en producción.

## Personalización

Edite el archivo `boda_data.json` para cambiar los nombres, fechas, frases y rutas de imágenes sin tocar el código fuente.