import shutil

formatting = {
    ".py": "Python",
    ".js": "JavaScript",
    ".html": "HTML",
    ".css": "CSS",
    ".java": "Java",
    ".ts": "TypeScript",
    ".jsx": "JSX",
    ".tsx": "TSX",
    ".scss": "SCSS",
    ".c": "C",
    ".h": "C/C++ Header",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    "others": "Others",
}


def formatear_estadisticas(stats):
    ancho = shutil.get_terminal_size().columns

    resultado = []
    resultado.append("\033[1mSTATS:\033[0m")
    resultado.append("-" * ancho)
    resultado.append(f"Files: {stats['files']}")
    resultado.append(f"Lines: {stats['lines']}")
    resultado.append("")
    resultado.append("Languages:")

    for stat in stats:
        if stat not in {"files", "lines"} and stats[stat] != 0:

            if stats["files"] > 0:
                porcentaje = (stats[stat] / stats["files"]) * 100
            else:
                porcentaje = 0

            resultado.append(
                f"  {formatting[stat]:<15}"
                f"{stats[stat]:<5}"
                f"{porcentaje:.1f}%"
            )

    return "\n".join(resultado)


def formatear_estadisticas_global(proyectos):
    stats = {
        extension: 0
        for extension in formatting
    }

    stats["files"] = 0
    stats["lines"] = 0

    for proyecto in proyectos.values():
        stats["files"] += proyecto["files"]
        stats["lines"] += proyecto["lines"]

        for lenguaje in proyecto["languages"]:
            if lenguaje in stats:
                stats[lenguaje] += proyecto["languages"][lenguaje]

    return formatear_estadisticas(stats)