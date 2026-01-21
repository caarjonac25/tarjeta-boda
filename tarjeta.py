from flask import Flask, render_template
import os

app = Flask(__name__)

# Datos de la boda
DATOS_BODA = {
    "novios": "Laura & Carlos",
    "fecha_texto": "Domingo, 28 de Junio de 2026",
    "hora": "4:00 pm",
    "lugar": "La Ruitoca, Bucaramanga",
    "direccion": "Av. Siempre Viva 123, Ciudad de México",
    "fecha_iso": "2026-06-28T16:00:00"
}

@app.route('/')
def home():
    return render_template('index.html', boda=DATOS_BODA)

if __name__ == '__main__':
    # Configuración para Render (usa la variable de entorno PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)