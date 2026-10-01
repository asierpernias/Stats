from stats.Formatter import formatear_estadisticas

def test_formatear_estadisticas():
    stats = {
            ".py": 0,
            ".js": 1,
            ".html": 1,
            ".css": 0,
            ".java": 0,
            "others": 2,
            "files": 2,
            "lines": 47
    }

    resultado = formatear_estadisticas(stats)

    assert "Files: 2" in resultado
    assert "Lines: 47" in resultado
    assert "Python" in resultado
    assert "Js" in resultado
    assert "Others" in resultado