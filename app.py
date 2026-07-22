from pathlib import Path


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
    
    elif size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes/1024:.2f} KB"

    elif size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes/(1024 ** 2):.2f} MB"

    return f"{size_in_bytes/(1024 ** 3):.2f} GB"


def display_file(files: list[Path]) -> None:
    """Display the scanned files."""

    print(f"\nDisplaying {len(files)} file(s):\n")

    print(f"{'Name':<30} {'Extension':<12} {'Size'}")
    print("-" * 60)

    for file in files:
        size = convert_file_size(file.stat().st_size)

        print(
            f"{file.name:<30}"
            f"{file.suffix:<12}"
            f"{size} bytes"
        )


def main() -> None:
    directory = get_directory_path()

    if not validate_directory(directory):
        print("\n✅ ❌ Invalid directory!")
        return

    print("\n✅ valid directory!")

    files = scan_directory(directory)
    display_file(files)

    print(f"\nFound {len(files)} file(s):\n")

    for file in files:
        print(file.name)


if __name__ == "__main__":
    main()
