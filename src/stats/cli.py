import argparse
from .analyzer import (
    analizar_carpeta,
    analizar_proyecto,
    calcular_estadisticas
)
from pathlib import Path

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

    proyecto = []
    if args.m == True:
        for path in args.paths:
            resultado =analizar_proyecto(Path(path))
            proyecto.append(resultado)
        
    else:
        for path in args.paths:
            resultado =analizar_carpeta(Path(path))
            proyecto.extend(resultado)
    estadisticas = calcular_estadisticas(proyecto)
    print(estadisticas)

if __name__ == "__main__":
    main()
