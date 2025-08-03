# main.py
from flask import Flask, request, jsonify
from mcp.core import procesar_mensaje

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def mcp():
    data = request.json
    mensaje_usuario = data.get("mensaje", "")
    usuario_id = data.get("usuario_id", 11)  
    respuesta = procesar_mensaje(mensaje_usuario, usuario_id)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)