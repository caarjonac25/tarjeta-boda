from flask import Flask, render_template
import os

app = Flask(__name__)

# Datos de la boda
DATOS_BODA = {
    "novios": "Ana & Carlos",
    "fecha_texto": "Sábado, 14 de Diciembre de 2024",
    "hora": "18:00 hrs",
    "lugar": "Hacienda El Ensueño",
    "direccion": "Av. Siempre Viva 123, Ciudad de México",
    "fecha_iso": "2024-12-14T18:00:00" 
}

@app.route('/')
def home():
    return render_template('index.html', boda=DATOS_BODA)

if __name__ == '__main__':
    # Configuración para Render (usa la variable de entorno PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)