from mcp.database import obtener_datos_usuario

def cargar_contexto_basico(usuario_id=11):
    datos = obtener_datos_usuario(usuario_id)

    if not datos:
        nombre = "usuario"
        datos_extra = ""
    else:
        nombre = datos["nombre"] or "usuario"

      
        enfermedades_lista = datos.get("enfermedades", [])
        enfermedades_texto = ", ".join(enfermedades_lista) if enfermedades_lista else "no especificadas"

        datos_extra = (
            f"Tiene {datos['edad']} años. "
            f"Enfermedades: {enfermedades_texto}. "
            f"Observaciones: {datos['observaciones'] or 'ninguna'}."
        )

    return [
        {"role": "system", "content": f"Eres un asistente personalizado que ayuda a una persona mayor llamada {nombre}."},
        {"role": "system", "content": f"{datos_extra} Recuerda hablar con amabilidad y explicar las cosas con claridad."}
    ]
