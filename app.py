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

def display_file(files: list[Path]) -> None:
    """Display the scanned files."""

    print(f"\nDisplaying {len(files)} file(s):\n")

    for file in files:
        print(file.name)


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
