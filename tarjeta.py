from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# Cargar datos de la boda desde un archivo JSON
with open('boda_data.json', 'r', encoding='utf-8') as f:
    DATOS_BODA = json.load(f)

@app.route('/')
def home():
    # Capturar parámetros de la URL (ej: ?n=2 pases&m=Familia Perez)
    pases = request.args.get('n', '')
    invitado = request.args.get('m', 'Invitado Especial')
    return render_template('index.html', boda=DATOS_BODA, pases=pases, invitado=invitado)

if __name__ == '__main__':
    # Configuración para Vercel/Render (usa la variable de entorno PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)