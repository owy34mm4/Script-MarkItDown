# PDF to Markdown Converter

Convierte archivos PDF a Markdown usando **[MarkItDown](https://github.com/microsoft/markitdown)**, la herramienta oficial de Microsoft para conversión de documentos.

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

Esto crea el entorno virtual `.venv` e instala todas las dependencias automáticamente.

---

## Uso

```
uv run python convert_pdf.py <pdf_path> [destiny_path]
```

### Argumentos

| Argumento      | Requerido | Descripción |
|----------------|-----------|-------------|
| `pdf_path`     | Sí        | Ruta completa al archivo PDF a convertir |
| `destiny_path` | No        | Ruta de destino para el `.md` generado   |

**Comportamiento de `destiny_path`:**
- **Omitido** → el `.md` se guarda en el mismo directorio del PDF
- **Directorio** → el `.md` se guarda dentro con el mismo nombre del PDF
- **Ruta `.md`** → usa ese nombre y ruta exactos

---

## Ejemplos

```bash
# Guardar el .md en la misma carpeta del PDF
uv run python convert_pdf.py "C:\docs\informe.pdf"

# Guardar el .md en un directorio distinto
uv run python convert_pdf.py "C:\docs\informe.pdf" "C:\output"

# Guardar el .md con nombre personalizado
uv run python convert_pdf.py "C:\docs\informe.pdf" "C:\output\informe_convertido.md"

# Ver ayuda
uv run python convert_pdf.py --help
```

---

## Estructura del proyecto

```
pdf-converter/
├── convert_pdf.py    # Script principal de conversión
├── pyproject.toml    # Configuración del proyecto y dependencias (uv)
├── requirements.txt  # Lista de dependencias (referencia)
├── uv.lock           # Lock file de uv (versiones exactas)
├── .venv/            # Entorno virtual (generado por uv sync)
├── README.md         # Esta documentación
└── CLAUDE.md         # Documentación técnica para Claude
```

---

## Dependencias principales

- [`markitdown[all]`](https://github.com/microsoft/markitdown) — Microsoft MarkItDown (conversión de documentos)
- [`pillow`](https://pillow.readthedocs.io/) — Procesamiento de imágenes

---

## Notas

- El archivo `.md` resultante se guarda en **UTF-8**.
- Compatible con Windows, macOS y Linux.
- Si el `destiny_path` no existe como directorio, se crea automáticamente.
