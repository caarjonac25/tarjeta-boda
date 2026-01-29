from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Datos de la boda
DATOS_BODA = {
    "novios": "Laura & Carlos",
    "fecha_texto": "Domingo, 28 de Junio de 2026",
    "fecha_dia": "28",
    "fecha_mes": "JUN",
    "fecha_anio": "2026",
    "hora": "4:00 pm",
    "lugar": "La Ruitoca, Bucaramanga",
    "direccion": "Km 2 Vía Ruitoque, Bucaramanga, Santander",
    "ubicacion_url": "https://www.google.com/maps/search/?api=1&query=La+Ruitoca+Bucaramanga",
    "ceremonia_lugar": "Capilla San José",
    "ceremonia_direccion": "Seminario Mayor Arquidiocesano",
    "ceremonia_url": "https://www.google.com/maps/place/Capilla+San+Jos%C3%A9+-+Seminario+Mayor+Arquidiocesano/@7.059459,-73.0809005,17z/data=!3m1!4b1!4m6!3m5!1s0x8e68409f7a4a7513:0x19ebdf17fb23a74a!8m2!3d7.0594537!4d-73.0783202!16s%2Fg%2F11c6ddsbmc?entry=ttu&g_ep=EgoyMDI2MDExOS4wIKXMDSoKLDEwMDc5MjA3MUgBUAM%3D",
    "fecha_iso": "2026-06-28T16:00:00",
    "frase": "El amor es paciente, es bondadoso. El amor no es envidioso ni jactancioso ni orgulloso. No se comporta con rudeza, no es egoísta, no se enoja fácilmente, no guarda rencor.",
    "itinerario": [
        {"hora": "4:00 PM", "actividad": "Ceremonia Religiosa", "icono": "fas fa-church"},
        {"hora": "5:30 PM", "actividad": "Cóctel de Bienvenida", "icono": "fas fa-glass-cheers"},
        {"hora": "6:30 PM", "actividad": "Recepción y Cena", "icono": "fas fa-utensils"},
        {"hora": "8:00 PM", "actividad": "Fiesta", "icono": "fas fa-music"},
    ],
    "regalos": {
        "frase": "Tu presencia es nuestro mejor regalo, pero si deseas tener un detalle con nosotros, agradecemos tu aporte en sobre.",
        "tipo": "Lluvia de Sobres"
    },
    "musica": "music/cancion1.mpeg",
    "dress_code": "Formal / Casual",
    "fotos": {
        "portada": "https://images.unsplash.com/photo-1519741497674-611481863552?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
        "galeria": [
            "https://images.unsplash.com/photo-1606800052052-a08af7148866?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        ]
    }
}

@app.route('/')
def home():
    # Capturar parámetros de la URL (ej: ?n=2 pases&m=Familia Perez)
    pases = request.args.get('n', '')
    invitado = request.args.get('m', 'Invitado Especial')
    return render_template('index.html', boda=DATOS_BODA, pases=pases, invitado=invitado)

if __name__ == '__main__':
    # Configuración para Render (usa la variable de entorno PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)