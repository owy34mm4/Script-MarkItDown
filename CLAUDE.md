# CLAUDE.md — MarkItDown Universal Converter

## Contexto del proyecto

Herramienta CLI en Python que pre-procesa documentos a Markdown usando **MarkItDown oficial de Microsoft** (`microsoft/markitdown`), antes de enviarlos a un LLM. Soporta PDF, DOCX, PPTX, XLSX, HTML, imágenes y más. El objetivo es reducir tokens y costo de procesamiento.

El proyecto usa **uv (Astral)** como gestor de paquetes y entornos virtuales.

---

## Cómo ejecutar

Siempre desde la carpeta `pdf-converter/` usando `uv run`:

```bash
uv run python convert_to_md.py <input_path> [destiny_path]
```

**Nunca** usar `python` directamente — se debe usar `uv run` para respetar el `.venv` gestionado por uv.

---

## Archivos del proyecto

| Archivo            | Propósito |
|--------------------|-----------|
| `convert_to_md.py` | Script principal. Acepta `input_path` y `destiny_path` por `sys.argv`. |
| `pyproject.toml`   | Definición del proyecto para uv. Contiene dependencias y versión de Python. |
| `uv.lock`          | Lock file con versiones exactas. No editar manualmente. |
| `requirements.txt` | Referencia de dependencias en formato pip (secundario). |
| `.venv/`           | Entorno virtual generado por `uv sync`. No commitear. |

---

## API de MarkItDown

```python
from markitdown import MarkItDown

converter = MarkItDown()
result = converter.convert("ruta/al/archivo")  # cualquier formato soportado
markdown_text = result.text_content            # str con el contenido Markdown
```

- No se valida la extensión — MarkItDown detecta el formato internamente
- El paquete correcto es `markitdown[all]` (incluye todos los extras)

---

## Notas técnicas

- **Codificación:** se fuerza UTF-8 en stdout para Windows (`sys.stdout = io.TextIOWrapper(...)`)
- **Python mínimo:** 3.10 (requerido por `markitdown`)
- **destiny_path:** puede ser directorio o ruta `.md`; se crea con `mkdir(parents=True)` si no existe
- **Sin validación de extensión:** MarkItDown maneja internamente los formatos; el script no restringe tipos
- **Salida:** siempre escrita en UTF-8

---

## Comandos útiles

```bash
# Instalar dependencias
uv sync

# Convertir cualquier documento
uv run python convert_to_md.py "ruta/al/archivo.pdf"
uv run python convert_to_md.py "ruta/al/archivo.docx" "ruta/destino"

# Ver ayuda
uv run python convert_to_md.py --help

# Agregar nueva dependencia
uv add <paquete>
```
