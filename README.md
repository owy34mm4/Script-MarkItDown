# MarkItDown Universal Converter

Pre-procesa documentos a Markdown usando **[MarkItDown](https://github.com/microsoft/markitdown)**, la herramienta oficial de Microsoft, antes de enviarlos a un LLM — ahorrando tokens y reduciendo costo de procesamiento.

---

## Formatos soportados

| Categoría    | Formatos                              |
|--------------|---------------------------------------|
| Documentos   | PDF, DOCX, PPTX, XLSX, ODT            |
| Web          | HTML, XML                             |
| Datos        | CSV, JSON                             |
| Imágenes     | JPG, PNG, GIF, BMP, TIFF (OCR/desc.)  |
| Audio        | MP3, WAV (transcripción)              |
| Otros        | ZIP, EPUB y más                       |

---

## Requisitos

| Herramienta | Versión mínima |
|-------------|----------------|
| Python      | >= 3.10        |
| uv (Astral) | cualquiera     |

> Instalar `uv`: https://docs.astral.sh/uv/getting-started/installation/

---

## Instalación

```bash
# Desde la carpeta pdf-converter/
uv sync
```

Crea el entorno virtual `.venv` e instala todas las dependencias automáticamente.

---

## Uso

```
uv run python convert_to_md.py <input_path> [destiny_path]
```

### Argumentos

| Argumento      | Requerido | Descripción |
|----------------|-----------|-------------|
| `input_path`   | Sí        | Ruta al archivo a convertir |
| `destiny_path` | No        | Ruta de destino para el `.md` generado |

**Comportamiento de `destiny_path`:**
- **Omitido** → el `.md` se guarda en el mismo directorio del input
- **Directorio** → el `.md` se guarda dentro con el mismo nombre del input
- **Ruta `.md`** → usa ese nombre y ruta exactos

---

## Ejemplos

```bash
# PDF → mismo directorio
uv run python convert_to_md.py "C:\docs\informe.pdf"

# DOCX → directorio distinto
uv run python convert_to_md.py "C:\docs\reporte.docx" "C:\output"

# PPTX → nombre personalizado
uv run python convert_to_md.py "C:\docs\slides.pptx" "C:\output\slides_converted.md"

# Ver ayuda
uv run python convert_to_md.py --help
```

---

## Flujo típico como pre-procesador LLM

```
documento (PDF/DOCX/PPTX...)
        ↓
convert_to_md.py
        ↓
archivo.md (texto limpio, sin ruido binario)
        ↓
LLM (menos tokens, menor costo)
```

---

## Estructura del proyecto

```
pdf-converter/
├── convert_to_md.py  # Script principal de conversión
├── pyproject.toml    # Configuración del proyecto y dependencias (uv)
├── requirements.txt  # Lista de dependencias (referencia)
├── uv.lock           # Lock file de uv (versiones exactas)
├── .venv/            # Entorno virtual (generado por uv sync)
├── README.md         # Esta documentación
└── CLAUDE.md         # Documentación técnica para Claude
```

---

## Dependencias principales

- [`markitdown[all]`](https://github.com/microsoft/markitdown) — Microsoft MarkItDown
- [`pillow`](https://pillow.readthedocs.io/) — Procesamiento de imágenes
