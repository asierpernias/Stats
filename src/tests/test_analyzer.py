from pathlib import Path
from stats.analyzer import analizar_proyecto, calcular_estadisticas

def text_calcular_estadisticas(tmp_path):
    (tmp_path / "main.py").write_text(
        "print('hello')\nprint('world')\n",
        encoding="utf-8"
    )

    proyecto = analizar_proyecto(tmp_path)
    stats = calcular_estadisticas([proyecto])

    assert stats[".py"] == 1
    assert stats["files"] == 1
    assert stats["files"] == 1

def test_analizar_proyecto(tmp_path):
    (tmp_path / "main.py").write_text(
        "print('hello')\nprint('world')\n",
        encoding="utf-8"
    )

    (tmp_path / "script.js").write_text(
        "console.log('hello');",
        encoding="utf-8"
    )

    proyecto = analizar_proyecto(tmp_path)

    lenguaje, files, lines = proyecto

    assert ".py" in lenguaje
    assert ".js" in lenguaje
    assert lines == 3
    assert files == 2


def test_carpeta_vacia(tmp_path):
    proyecto = analizar_proyecto(tmp_path)

    lenguajes, files, lines = proyecto
    assert files ==0
    assert lines == 0
    assert lenguajes == set()