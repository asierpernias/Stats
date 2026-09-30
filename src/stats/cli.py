import argparse
from pathlib import Path

from .analyzer import (
    analizar_carpeta,
    analizar_proyecto,
    calcular_estadisticas
)
from .Formatter import formatear_estadisticas


def main():
    
    parser = argparse.ArgumentParser(
        description="Analyze programming projects",
    )

    parser.add_argument(
        "paths",
        nargs="*",
    )

    parser.add_argument(
        "-m",
        action="store_true"
    )

    args = parser.parse_args()
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
        
    else:
        for path in rutas:
            resultado =analizar_carpeta(Path(path))
            proyecto.extend(resultado)
    estadisticas = calcular_estadisticas(proyecto)
    print(formatear_estadisticas(estadisticas))

if __name__ == "__main__":
    main()
