from pathlib import Path


def get_directory_path() -> Path:
    """Ask the user to enter a directory path."""

    directory = input("Enter directory path: ").strip()
    return Path(directory)

def validate_directory(path: Path) -> bool:
    """Validate whether the given path is an existing directory."""
    return path.exists() and path.is_dir()

def main() -> None:
    directory = get_directory_path()
    if validate_directory(directory):
        print("\n✅ Valid directory!")
    else:
        print("\n❌ Invalid directory!")


if __name__ == "__main__":
    main()
