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
    resultado.append("STATS:")
    resultado.append("-" * ancho)
    for stat in stats:
        resultado.append(f"{formatting[stat] :<12} {stats[stat] }")

    return "\n".join(resultado)