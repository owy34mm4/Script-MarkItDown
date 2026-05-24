#!/usr/bin/env python3
"""
Script para convertir PDF a Markdown usando MarkItDown de Microsoft.
Procesa un PDF especificado y genera un archivo Markdown en el destino indicado.

Uso:
    uv run python convert_pdf.py <pdf_path> [destiny_path]

Argumentos:
    pdf_path      Ruta completa al archivo PDF a convertir (requerido)
    destiny_path  Ruta del directorio o archivo .md de salida (opcional)
                  Si no se indica, el .md se guarda en el mismo directorio del PDF
"""

import sys
from pathlib import Path
from markitdown import MarkItDown

# Configurar codificación UTF-8 para stdout en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HELP_TEXT = """
MarkItDown PDF to Markdown Converter - Microsoft
================================================

Uso:
  uv run python convert_pdf.py <pdf_path> [destiny_path]

Argumentos:
  pdf_path      Ruta al archivo PDF a convertir (requerido)
  destiny_path  Ruta de destino para el archivo .md (opcional)
                - Si es un directorio: guarda el .md dentro con el mismo nombre del PDF
                - Si es una ruta .md: usa ese nombre exacto
                - Si se omite: guarda en el mismo directorio del PDF

Ejemplos:
  uv run python convert_pdf.py "C:/docs/archivo.pdf"
  uv run python convert_pdf.py "C:/docs/archivo.pdf" "C:/output"
  uv run python convert_pdf.py "C:/docs/archivo.pdf" "C:/output/resultado.md"
"""


def resolve_output_path(pdf_file: Path, destiny_path: str | None) -> Path:
    """
    Resuelve la ruta de salida del archivo Markdown.

    Args:
        pdf_file:     Path del PDF de entrada
        destiny_path: Argumento de destino (puede ser dir, archivo .md o None)

    Returns:
        Path completo del archivo .md de salida
    """
    if not destiny_path:
        return pdf_file.parent / (pdf_file.stem + ".md")

    dest = Path(destiny_path)

    # Si es un directorio existente o termina sin extensión (asumimos directorio)
    if dest.is_dir() or not dest.suffix:
        dest.mkdir(parents=True, exist_ok=True)
        return dest / (pdf_file.stem + ".md")

    # Si termina en .md u otra extensión, usar esa ruta directamente
    dest.parent.mkdir(parents=True, exist_ok=True)
    return dest


def convert_pdf_to_markdown(pdf_path: str, destiny_path: str | None = None) -> None:
    """
    Convierte un archivo PDF a Markdown usando MarkItDown de Microsoft.

    Args:
        pdf_path:     Ruta completa al archivo PDF a convertir
        destiny_path: Ruta de destino para el archivo .md (opcional)

    Raises:
        FileNotFoundError: Si el archivo PDF no existe
        ValueError:        Si la ruta no corresponde a un PDF
        Exception:         Si hay error durante la conversión
    """
    pdf_file = Path(pdf_path).resolve()

    if not pdf_file.exists():
        raise FileNotFoundError(f"El archivo PDF no existe: {pdf_path}")

    if pdf_file.suffix.lower() != '.pdf':
        raise ValueError(f"El archivo no es un PDF: {pdf_path}")

    markdown_path = resolve_output_path(pdf_file, destiny_path)

    print(f"[*] PDF de entrada:  {pdf_file}")
    print(f"[*] Destino del .md: {markdown_path}")
    print("[*] Convirtiendo...")

    converter = MarkItDown()
    result = converter.convert(str(pdf_file))

    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(result.text_content)

    file_size_kb = markdown_path.stat().st_size / 1024
    print(f"[OK] Archivo generado: {markdown_path.name}  ({file_size_kb:.2f} KB)")


def main():
    """Función principal — valida argumentos y ejecuta la conversión."""
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)

    pdf_path     = args[0]
    destiny_path = args[1] if len(args) > 1 else None

    print("=" * 60)
    print("MarkItDown PDF to Markdown Converter - Microsoft")
    print("=" * 60)

    try:
        convert_pdf_to_markdown(pdf_path, destiny_path)
        print("\n[OK] Proceso completado sin errores.")
    except (FileNotFoundError, ValueError) as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
