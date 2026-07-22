from pathlib import Path

FILE_CATEGORIES = {
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Music": {".mp3", ".wav", ".aac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".cs"},
}


def get_directory_path() -> Path:
    """Ask the user to enter a directory path."""

    directory = input("Enter directory path: ").strip()
    return Path(directory)


def validate_directory(path: Path) -> bool:
    """Validate whether the given path is an existing directory."""
    return path.exists() and path.is_dir()


def scan_directory(path: Path) -> list[Path]:
    """Return all files inside the given directory."""
    files = []

    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    return files


def convert_file_size(size_in_bytes: int) -> str:
    """Convert file size from bytes to human-readable format."""

    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"

    elif size_in_bytes < 1024**2:
        return f"{size_in_bytes / 1024:.2f} KB"

    elif size_in_bytes < 1024**3:
        return f"{size_in_bytes / (1024**2):.2f} MB"

    return f"{size_in_bytes / (1024**3):.2f} GB"


def get_file_category(file: Path) -> str:
    """Return the category of a file based on its extension."""

    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def truncate_text(text: str, max_length: int) -> str:
    if max_length <= 3:
        return "." * max_length
    elif len(text) <= max_length:
        return text

    return text[: max_length - 3] + "..."


def display_file(files: list[Path]) -> None:
    """Display the scanned files."""

    print(f"\nDisplaying {len(files)} file(s):\n")

    print(f"{'Name':<40} {'Extension':<12} {'Category':<15} {'Size'}")
    print("-" * 80)

    for file in files:
        size = convert_file_size(file.stat().st_size)
        category = get_file_category(file)

        print(f"{truncate_text(file.stem, 35):<40}{file.suffix:<12}{category:<15}{size}")


def main() -> None:
    directory = get_directory_path()

    if not validate_directory(directory):
        print("\n✅ ❌ Invalid directory!")
        return

    print("\n✅ valid directory!")

    files = scan_directory(directory)
    display_file(files)

    # print(f"\nFound {len(files)} file(s):\n")

    # for file in files:
    #     print(file.name)


if __name__ == "__main__":
    main()
