import shutil

formatting = {
    ".py": "Python",
    ".js": "Js",
    ".html": "Html",
    ".css": "CSS",
    ".java": "Java",
    ".ts": "TSX",
    ".jsx": "JSX",
    ".tsx": "TSX",
    ".scss":"SCSS",
    ".c": "C",
    ".h": "C/C++ Header",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
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
        ".ts": 0,
        ".jsx": 0,
        ".tsx": 0,
        ".scss":0,
        ".c": 0,
        ".h": 0,
        ".cpp": 0,
        ".cs": 0,
        ".go": 0,
        ".rs": 0,
        "others": 0
    }

    for proyecto in proyectos.values():
        stats["files"] += proyecto["files"]
        stats["lines"] += proyecto["lines"]

        for lenguaje in proyecto["languages"]:
            if lenguaje in stats:
                stats[lenguaje] += proyecto["languages"][lenguaje]

    return formatear_estadisticas(stats)