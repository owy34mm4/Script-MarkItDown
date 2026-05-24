# CLAUDE.md — PDF to Markdown Converter

## Contexto del proyecto

Herramienta CLI en Python para convertir archivos PDF a Markdown usando **MarkItDown de Microsoft** (`microsoft/markitdown`). Desarrollada en el contexto académico de la materia Diseño de Software (Iberoamericana).

El proyecto usa **uv (Astral)** como gestor de paquetes y entornos virtuales.

---

## Cómo ejecutar

Siempre ejecutar desde la carpeta `pdf-converter/` usando `uv run`:

```bash
uv run python convert_pdf.py <pdf_path> [destiny_path]
```

**Nunca** usar `python` directamente — se debe usar `uv run` para que tome el entorno `.venv` gestionado por uv.

---

## Archivos del proyecto

| Archivo           | Propósito |
|-------------------|-----------|
| `convert_pdf.py`  | Script principal. Acepta `pdf_path` y `destiny_path` por `sys.argv`. |
| `pyproject.toml`  | Definición del proyecto para uv. Contiene dependencias y versión de Python. |
| `uv.lock`         | Lock file con versiones exactas de todas las dependencias. No editar manualmente. |
| `requirements.txt`| Referencia de dependencias en formato pip (secundario, uv usa pyproject.toml). |
| `.venv/`          | Entorno virtual generado por `uv sync`. No commitear. |

---

## API de MarkItDown

```python
from markitdown import MarkItDown

converter = MarkItDown()
result = converter.convert("ruta/al/archivo.pdf")
markdown_text = result.text_content  # str con el contenido Markdown
```

- `MarkItDown()` — instancia sin argumentos
- `.convert(path: str)` — retorna un objeto con atributo `.text_content`
- El paquete correcto es `markitdown[all]` (incluye soporte para PDF, DOCX, imágenes, etc.)

---

## Notas técnicas

- **Codificación:** se fuerza UTF-8 en stdout para Windows (`sys.stdout = io.TextIOWrapper(...)`)
- **Python mínimo:** 3.10 (requerido por `markitdown`)
- **destiny_path:** puede ser directorio o ruta `.md`; si el directorio no existe, se crea con `mkdir(parents=True)`
- **Salida:** siempre escrita en UTF-8 (`open(..., encoding='utf-8')`)

---

## Comandos útiles

```bash
# Instalar dependencias
uv sync

# Ejecutar conversión
uv run python convert_pdf.py "..\mi_archivo.pdf"
uv run python convert_pdf.py "..\mi_archivo.pdf" "..\salida"

# Ver ayuda
uv run python convert_pdf.py --help

# Agregar nueva dependencia
uv add <paquete>
```
