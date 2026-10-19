ESPECIALIDADES = [
    {
        "nombre": "Desarrollo de Software",
        "descripcion": "Aprende a programar y construir aplicaciones.",
        "nivel": "Inicial e intermedio",
    },
    {
        "nombre": "Sistemas",
        "descripcion": "Explora equipos, redes y servicios tecnológicos.",
        "nivel": "Inicial e intermedio",
    },
    {
        "nombre": "Diseño Digital",
        "descripcion": "Desarrolla soluciones visuales y creativas.",
        "nivel": "Inicial",
    },
]


def listar_especialidades():
    """Devuelve la lista completa de especialidades."""
    return ESPECIALIDADES.copy()


def buscar_especialidades(texto):
    """Busca especialidades por nombre o descripción."""
    consulta = texto.strip().casefold()
    if not consulta:
        return listar_especialidades()

    return [
        item for item in ESPECIALIDADES
        if consulta in item["nombre"].casefold()
        or consulta in item["descripcion"].casefold()
    ]