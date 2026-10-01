import json
from pathlib import Path

STATS_FILE = Path.home() / ".stats" / "projects.json"


def cargar_proyecto():
    if not STATS_FILE.exists():
            return {}
    with STATS_FILE.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_proyecto(nombre, files, lines, languages):
    proyectos = cargar_proyecto()

    proyectos[nombre] = {
         "files": files,
         "lines": lines,
         "languages": languages
    }

    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with STATS_FILE.open("w", encoding="utf-8") as archivo:
         json.dump(proyectos, archivo, indent=4)

def listar_proyectos():
     proyectos = cargar_proyecto()
     return list(proyectos.keys())

def eliminar_proyecto(nombre):
    proyectos = cargar_proyecto()

    if not nombre in proyectos:
        return False

    del proyectos[nombre]

    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)   

    with STATS_FILE.open("w", encoding="utf-8") as archivo:
        json.dump(proyectos, archivo, indent=4)

    return True