
from pathlib import Path
import sys
import os

SUFIXES = {
    ".py": 0,
    ".js": 0,
    ".html": 0,
    ".css": 0,
    ".java": 0,
    "others": 0
}
def recorrer_archivos(carpeta, proyecto):
    contador = 0
    lineas = 0
    for item in carpeta.iterdir():

        if item.is_dir():

            if item.name == ".git":
                continue

            archivo_subcarpeta, lineas_subcarpeta = recorrer_archivos(item, proyecto)
            lineas += lineas_subcarpeta
            contador += archivo_subcarpeta
        else:
            extension = item.suffix
            contador += 1
            if extension in SUFIXES:
                SUFIXES[extension] += 1
                proyecto.add(extension)
                contenido = item.read_text(encoding="utf-8")
                lineas += len(contenido.splitlines())

            else:
                SUFIXES["others"] += 1
                proyecto.add("others")
    return contador, lineas
    
def analizar_carpeta(carpeta):
    proyectos = []

    for item in carpeta.iterdir():

        if item.is_dir():

            proyecto = analizar_proyecto(item)
            proyectos.append(proyecto)

    return proyectos

def analizar_proyecto(carpeta):
    proyecto = set()

    contador, lineas = recorrer_archivos(carpeta, proyecto)

    return proyecto, contador, lineas

def calcular_estadisticas(proyectos):

    stats = {
        ".py": 0,
        ".js": 0,
        ".html": 0,
        ".css": 0,
        ".java": 0,
        "others": 0,
        "files": 0,
        "lines": 0
    }

    for proyecto, contador, lineas in proyectos:
        for lenguaje in proyecto:
            if lenguaje in stats:
                stats[lenguaje] +=1
        
        stats["files"] += contador
        stats["lines"] += lineas


    return stats

