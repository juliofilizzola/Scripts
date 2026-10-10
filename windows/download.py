from pathlib import Path
import shutil
from typing import Union

EXTENSION_CATEGORIES: dict[str, str] = {
    # Imagens -> Pictures / Imagens
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".bmp": "Images",
    ".ico": "Images",
    ".tiff": "Images",
    # Documentos -> Documents / Documentos
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".ppt": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    # Planilhas -> Documents / Documentos
    ".xlsx": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",
    # Compactados -> Documents / Documentos
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    # Mídia / Áudio -> Music / Músicas
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".wma": "Audio",
    ".m4a": "Audio",
    # Mídia / Vídeo -> Videos / Vídeos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    # Executáveis / Instaladores -> Mantidos em Downloads
    ".exe": "Executables",
    ".msi": "Executables",
}

CATEGORY_FOLDER_CANDIDATES: dict[str, list[str]] = {
    "Images": ["Pictures", "Imagens"],
    "Documents": ["Documents", "Documentos"],
    "Spreadsheets": ["Documents", "Documentos"],
    "Audio": ["Music", "Músicas", "Musicas"],
    "Videos": ["Videos", "Vídeos"],
    "Archives": ["Documents", "Documentos"],
    "Executables": ["Downloads"],
}


def get_standard_user_dir(category: str) -> Path:
    """
    Retorna o diretório padrão correspondente no sistema do usuário (Windows/Linux/macOS).
    Verifica a existência das pastas conhecidas (inglês/português) dentro de Path.home().
    """
    home = Path.home()
    candidates = CATEGORY_FOLDER_CANDIDATES.get(category, ["Downloads"])

    for candidate in candidates:
        candidate_path = home / candidate
        if candidate_path.exists() and candidate_path.is_dir():
            return candidate_path.resolve()

    # Se não existir, utiliza o primeiro candidato e o cria
    target_path = (home / candidates[0]).resolve()
    target_path.mkdir(parents=True, exist_ok=True)
    return target_path


def _get_unique_destination_path(target_dir: Path, filename: str) -> Path:
    """Gera um caminho único adicionando sufixo numérico caso já exista um arquivo com mesmo nome."""
    destination = target_dir / filename
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1
    while destination.exists():
        destination = target_dir / f"{stem} ({counter}){suffix}"
        counter += 1
    return destination


def clean_download_dir(directory_path: Union[str, Path, None] = None) -> None:
    """
    Organiza os arquivos de Downloads enviando-os para os diretórios padrão do Windows
    (Imagens, Documentos, Músicas, Vídeos, etc.) em vez de criar subpastas em Downloads.
    
    :param directory_path: Caminho para a pasta de origem a ser organizada (padrão: Downloads do usuário).
    """
    if directory_path is None:
        source_dir = (Path.home() / "Downloads").resolve()
    else:
        source_dir = Path(directory_path).expanduser().resolve()

    print(f"Verificando diretório de origem: {source_dir}")

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Diretório não encontrado: {source_dir}")
        return

    moved_count = 0

    for file_path in source_dir.iterdir():
        # Ignora diretórios existentes para não mover pastas
        if not file_path.is_file():
            continue

        category = EXTENSION_CATEGORIES.get(file_path.suffix.lower(), "Others")
        target_dir = get_standard_user_dir(category)

        # Se o destino for o próprio diretório de origem, não move
        if target_dir == source_dir:
            continue

        destination_path = _get_unique_destination_path(target_dir, file_path.name)

        try:
            shutil.move(file_path, destination_path)
            print(f"Movido: '{file_path.name}' -> {target_dir}")
            moved_count += 1
        except OSError as error:
            print(f"Erro ao mover '{file_path.name}' para '{target_dir}': {error}")

    print(f"Organização concluída: {moved_count} arquivo(s) organizado(s).")


if __name__ == "__main__":
    clean_download_dir()