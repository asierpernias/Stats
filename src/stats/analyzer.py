
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
    for item in carpeta.iterdir():

        if item.is_dir():

            if item.name == ".git":
                continue

            recorrer_archivos(item, proyecto)

        else:
            extension = item.suffix

            if extension in SUFIXES:
                SUFIXES[extension] += 1
                proyecto.add(extension)

            else:
                SUFIXES["others"] += 1
    
def analizar_carpeta(carpeta):
    proyectos = []

    for item in carpeta.iterdir():

        if item.is_dir():

            proyecto = analizar_proyecto(item)
            proyectos.append(proyecto)

    return proyectos

def analizar_proyecto(carpeta):
    proyecto = set()

    recorrer_archivos(carpeta, proyecto)

    return proyecto

def calcular_estadisticas(proyectos):

    stats = {
        ".py": 0,
        ".js": 0,
        ".html": 0,
        ".css": 0,
        ".java": 0,
        "others": 0
    }

    for proyecto in proyectos:
        for lenguaje in proyecto:
            if lenguaje in stats:
                stats[lenguaje] +=1

    return stats

