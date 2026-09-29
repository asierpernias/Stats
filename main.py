from pathlib import Path
import sys
import os


directory = Path(input("What is the path you want to analise?: "))
sufixes = {
    ".py": 0,
    ".js": 0,
    ".html": 0,
    ".css": 0,
    ".java": 0,
    "others": 0
}
stats_generales = {
    ".py": 0,
    ".js": 0,
    ".html": 0,
    ".css": 0,
    ".java": 0,
    "others": 0
}
if directory.exists() and directory.is_dir():
    pass
else: 
    print("The give root is incorrect try again")
    sys.exit()

proyectos = []


def analizar(carpeta, profundidad, proyecto=None):

    for item in carpeta.iterdir():

        if item.is_dir():

            if item.name == ".git":
                continue

            profundidad += 1

            print("\t" * profundidad, item.relative_to(carpeta))

            analizar(item, profundidad, proyecto)

            profundidad -= 1
        else:
            root, extension = os.path.splitext(item) 

            if extension in sufixes:
                sufixes[extension] += 1
                proyecto.add(extension)
            else: 
                sufixes['others'] += 1

            print("\t" * profundidad, item.relative_to(carpeta))
    
for item in directory.iterdir():

    if item.is_dir():
        proyecto = set()
        print(item.name)
        analizar(item, 0, proyecto)
        proyectos.append(proyecto)

for proyecto in proyectos:
    for lenguaje in proyecto:
        if lenguaje in stats_generales:
            stats_generales[lenguaje] += 1

print("\nProyectos:")
print(proyectos)

print("\nStats de archivos:")
print(sufixes)

print("\nStats generales: ")
print(stats_generales)