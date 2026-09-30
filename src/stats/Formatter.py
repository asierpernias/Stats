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
    resultado.append(f"Lines: {stats['lineas']} \n")
    for stat in stats:
        if stat not in {"files", "lineas"}:
            resultado.append(f"{formatting[stat]:<12} {stats[stat] }")

    return "\n".join(resultado)