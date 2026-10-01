import argparse
from pathlib import Path

from .analyzer import (
    analizar_carpeta,
    analizar_proyecto,
    calcular_estadisticas
)
from .Formatter import formatear_estadisticas, formatear_estadisticas_global
from .storage import cargar_proyecto, guardar_proyecto

def main():
    
    parser = argparse.ArgumentParser(
        description="Analyze programming projects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
    stats 
    stats . 
    stats ./project 
    stats -m ./my-project 
    stats -m ./project-1 ./project-2 
    stats -m ./my-project --save 
    stats --global 

"""
    )

    parser.add_argument(
        "paths",
        nargs="*",
    )

    parser.add_argument(
        "-m",
        action="store_true"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="stats 0.2.0"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save project statistics locally"
    )

    parser.add_argument(
        "--global",
        dest="global_stats",
        action="store_true",
        help="Show statistics for all saved projects"
    )

    args = parser.parse_args()

    if args.global_stats:
        proyectos_guardados = cargar_proyecto()

        if not proyectos_guardados:
            print("No saved projects")
            return
        print(formatear_estadisticas_global(proyectos_guardados))
        return

    
    if not args.paths:
        args.paths = ["."]

    rutas = []
    proyecto = []

    for path in args.paths:
        path = Path(path)

        if not path.is_dir():
            print(f"Error: {path} is not a folder")
            continue

        rutas.append(path)

    if not rutas:
        raise SystemExit(1)

    if args.m:
      for path in rutas:
            resultado =analizar_proyecto(Path(path))
            proyecto.append(resultado)

            if args.save:
                estadisticas_proyecto = calcular_estadisticas([resultado])
                guardar_proyecto(
                    path.name,
                    estadisticas_proyecto["files"],
                    estadisticas_proyecto["lines"],
                {
                    lenguaje: estadisticas_proyecto[lenguaje]
                    for lenguaje in estadisticas_proyecto
                    if lenguaje not in ("files", "lines")
                }
            )
    else:
        for path in rutas:
            resultado =analizar_carpeta(Path(path))
            proyecto.extend(resultado)
    estadisticas = calcular_estadisticas(proyecto)    
    print(formatear_estadisticas(estadisticas))

if __name__ == "__main__":
    main()
