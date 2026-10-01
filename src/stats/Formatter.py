import shutil

formatting = {
    ".py": "Python",
    ".js": "Js",
    ".html": "Html",
    ".css": "CSS",
    ".java": "Java",
    "others": "Others"
}
def formatear_estadisticas(stats):
    ancho = shutil.get_terminal_size().columns
    resultado = []
    resultado.append("\033[1mSTATS:\033[0m")
    resultado.append("-" * ancho)
    resultado.append(f"Files: {stats['files']}")
    resultado.append(f"Lines: {stats['lines']} \n")
    for stat in stats:
        if stat not in {"files", "lines"}:
            resultado.append(f"{formatting[stat]:<12} {stats[stat] }")

    return "\n".join(resultado)

def formatear_estadisticas_global(proyectos):
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

    for proyecto in proyectos.values():
        stats["files"] += proyecto["files"]
        stats["lines"] += proyecto["lines"]

        for lenguaje in proyecto["languages"]:
            if lenguaje in stats:
                stats[lenguaje] += proyecto["languages"][lenguaje]

    return formatear_estadisticas(stats)