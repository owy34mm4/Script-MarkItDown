#!/usr/bin/env python3
"""
Conversor universal de documentos a Markdown usando MarkItDown de Microsoft.
Pre-procesa archivos antes de enviarlos a un LLM, reduciendo tokens y costo.

Formatos soportados: PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML,
                     imágenes, audio, ZIP, EPUB y más.

Uso:
    uv run python convert_to_md.py <input_path> [destiny_path]

Argumentos:
    input_path    Ruta al archivo a convertir (requerido)
    destiny_path  Ruta del directorio o archivo .md de salida (opcional)
                  Si no se indica, el .md se guarda en el mismo directorio del input
"""

import sys
from pathlib import Path
from markitdown import MarkItDown

# Configurar codificación UTF-8 para stdout en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HELP_TEXT = """
MarkItDown Universal Converter - Microsoft
==========================================
Pre-procesa documentos a Markdown para consumo eficiente por LLMs.

Uso:
  uv run python convert_to_md.py <input_path> [destiny_path]

Argumentos:
  input_path    Ruta al archivo a convertir (requerido)
  destiny_path  Ruta de destino para el archivo .md (opcional)
                - Si es un directorio: guarda el .md dentro con el mismo nombre del input
                - Si es una ruta .md: usa ese nombre exacto
                - Si se omite: guarda en el mismo directorio del input

Formatos soportados:
  PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML,
  imágenes (JPG, PNG, etc.), audio, ZIP, EPUB y más.

Ejemplos:
  uv run python convert_to_md.py "C:/docs/informe.pdf"
  uv run python convert_to_md.py "C:/docs/presentacion.pptx" "C:/output"
  uv run python convert_to_md.py "C:/docs/datos.xlsx" "C:/output/datos.md"
"""


def resolve_output_path(input_file: Path, destiny_path: str | None) -> Path:
    """
    Resuelve la ruta de salida del archivo Markdown.

    Args:
        input_file:   Path del archivo de entrada
        destiny_path: Argumento de destino (puede ser dir, archivo .md o None)

    Returns:
        Path completo del archivo .md de salida
    """
    if not destiny_path:
        return input_file.parent / (input_file.stem + ".md")

    dest = Path(destiny_path)

    if dest.is_dir() or not dest.suffix:
        dest.mkdir(parents=True, exist_ok=True)
        return dest / (input_file.stem + ".md")

    dest.parent.mkdir(parents=True, exist_ok=True)
    return dest


def convert_to_markdown(input_path: str, destiny_path: str | None = None) -> None:
    """
    Convierte un documento a Markdown usando MarkItDown de Microsoft.

    Args:
        input_path:   Ruta completa al archivo a convertir
        destiny_path: Ruta de destino para el archivo .md (opcional)

    Raises:
        FileNotFoundError: Si el archivo no existe
        Exception:         Si hay error durante la conversión
    """
    input_file = Path(input_path).resolve()

    if not input_file.exists():
        raise FileNotFoundError(f"El archivo no existe: {input_path}")

    markdown_path = resolve_output_path(input_file, destiny_path)

    print(f"[*] Entrada:  {input_file}")
    print(f"[*] Salida:   {markdown_path}")
    print("[*] Convirtiendo...")

    converter = MarkItDown()
    result = converter.convert(str(input_file))

    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(result.text_content)

    file_size_kb = markdown_path.stat().st_size / 1024
    print(f"[OK] Generado: {markdown_path.name}  ({file_size_kb:.2f} KB)")


def main():
    """Función principal — valida argumentos y ejecuta la conversión."""
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)

    input_path   = args[0]
    destiny_path = args[1] if len(args) > 1 else None

    print("=" * 60)
    print("MarkItDown Universal Converter - Microsoft")
    print("=" * 60)

    try:
        convert_to_markdown(input_path, destiny_path)
        print("\n[OK] Proceso completado sin errores.")
    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
