import json 
from stats import storage

def test_guardar_cargar_proyecto(tmp_path, monkeypatch):
    archivo = tmp_path / "projects.json"
    monkeypatch.setattr(
        storage,
        "STATS_FILE",
        archivo
    )

    storage.guardar_proyecto(
        "TestProject",
        10,
        100,
        {
            ".py":2,
            ".js":5
        }
    )

    proyectos = storage.cargar_proyecto()

    assert "TestProject" in proyectos
    assert proyectos["TestProject"]["files"] == 10
    assert proyectos["TestProject"]["lines"] == 100
    assert proyectos["TestProject"]["languages"][".py"] == 2
    assert proyectos["TestProject"]["languages"][".js"] == 5

